# ------------------------------------------------------------------------------
# Steel TTS
#
# license:       MIT License
#                Copyright (c) 2013-2014 Jasper R. Danielson
# website:       http://sourceforge.net/projects/steeltts/
# version:       0.3.0 (released 04/20/2014)
#
# ------------------------------------------------------------------------------
#
# file:          SAPI5.py
# purpose:       Provides a wrapper for Microsoft Speech API 5.x speech synthesis
# classes:       SAPI5
# functions:     None
#

import platform
import os
import math

if platform.system() == "Windows":
    try:
        import win32com.client
        import pythoncom
    except:
        pass

class SAPI5():
    '''Microsoft Speech API 5.x wrapper'''
    def __init__(self):
        if platform.system() != "Windows":
            raise RuntimeError("Microsoft Speech API 5.x is only available on Windows")
        try:
            pythoncom.CoInitialize()
            self.engine = win32com.client.Dispatch("SAPI.SPVoice")
            self._pitch = 0
            self.stop()
        except:
            raise ImportError("PyWin32 package not properly installed on this computer")

    def speak(self, text, interrupt=False):
        '''Speaks the given string of text'''
        if not isinstance(text, str):
            raise TypeError("Text must be of type \"string\"")
        if interrupt:
            self.stop()
        exec("text = \"<pitch absmiddle='%s'>%s\"" % (str(int(self._pitch)),text))
        self.engine.Speak(text,1)

    def stop(self):
        '''Halts any current speech events'''
        self.engine.Speak('',3)

    def available_voices(self):
        '''Returns a list of voices available for use with SAPI5'''
        voices = []
        for oo in self.engine.GetVoices():
            voices.append(oo.GetDescription())
        return voices

    def get(self, attribute):
        '''Returns the specified attribute

        Recognized attributes: pitch, rate, voice, volume'''
        attribute = attribute.lower()
        if attribute == "pitch":
            return int(round(float(self._pitch),0))
        elif attribute == "rate":
            return int(round((1.11**self.engine.Rate)*150,0))
        elif attribute == "volume":
            return self.engine.Volume
        elif attribute == "voice":
            return self.engine.Voice.GetDescription().encode("ascii")
        else:
            raise ValueError("\"%s\" not a recognized attribute" % (attribute))

    def set(self, attribute, value):
        '''Sets the specified attribute to the given value

        Recognized attributes: pitch, rate, voice, volume'''
        attribute = attribute.lower()
        if attribute == "pitch":
            if not isinstance(value,(int,float)):
                raise TypeError("pitch must be either an integer or floating point number")
            elif not -10 <= value <= 10:
                raise ValueError("pitch value must be in range -10--10")
            else:
                self._pitch = int(round(float(value),0))
        elif attribute == "rate":
            if not isinstance(value,(int,float)):
                raise TypeError("rate must be either an integer or floating point number")
            elif not 50 <= value <= 450:
                raise ValueError("rate value must be in range 50--450")
            else:
                self.engine.Rate = int(round(math.log(float(value)/150, 1.11),0))
        elif attribute == "volume":
            if not isinstance(value,(int,float)):
                raise TypeError("volume must be either an integer or floating point number")
            elif not 0 <= value <= 100:
                raise ValueError("volume value must be in range 0--100")
            else:
                self.engine.Volume = int(round(float(value), 2))
        elif attribute == "voice":
            if not isinstance(value,(int,str)):
                raise TypeError("voice must be of type \"string\"")
            else:
                set = False
                for oo in self.engine.GetVoices():
                    if oo.GetDescription() == value:
                        self.engine.Voice = oo
                        set = True
                if not set:
                    raise ValueError("Voice \"%s\" not available" % (value))
        else:
            raise ValueError("\"%s\" not a recognized attribute" % (attribute))

    def speak_to_wav(self, text, path):
        '''Speaks the given string of text to a .wav file and saves it to the given path'''
        #To do: Add support for non-WAV file types
        if not isinstance(path, str):
            raise TypeError("Path must be of type \"string\"")
        elif not isinstance(text, str):
            raise TypeError("Text must be of type \"string\"")
        elif path[-4:] != ".wav":
            raise ValueError("Path must specify a .wav file")
        path = os.path.expandvars(os.path.expanduser(path))
        path = os.path.abspath(path)
        path = os.path.normpath(path).replace("\\","/")
        folder = path.replace(path.split("/")[-1],"")
        if not os.path.isdir(folder):
            raise RuntimeError(".wav file must be placed in a valid directory")
        else:
            stream = win32com.client.Dispatch("SAPI.SpFileStream")
            stream.Open(path,3)
            self.engine.AudioOutputStream = stream
            exec("text = \"<pitch absmiddle='%s'>%s\"" % (str(int(self._pitch)),text))
            self.engine.Speak(text,0)
            stream.Close()