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
# file:          NSSS.py
# purpose:       Provides a wrapper for NSSpeechSynthesizer on Mac OS X
# classes:       NSSS
# functions:     None
#

import subprocess
import platform
import os

try:
    from AppKit import NSSpeechSynthesizer
except ImportError:
    try:
        from Cocoa import NSSpeechSynthesizer
    except:
        pass

class NSSS():
    '''NSSpeechSynthesis wrapper'''
    def __init__(self):
        if platform.system() != "Darwin":
            raise RuntimeError("NSSpeechSynthesizer wrapper only available on Mac OS X")
        try:
            from AppKit import NSSpeechSynthesizer
        except ImportError:
            try:
                from Cocoa import NSSpeechSynthesizer
            except:
                raise ImportError("NSSpeechSynthesizer not properly installed on this computer")
        self.tts = NSSpeechSynthesizer.alloc().initWithVoice_(None)

    def speak(self, text, interrupt=False):
        '''Speaks the given string of text'''
        if not isinstance(text, str):
            raise TypeError("Text must be of type \"string\"")
        if interrupt:
            self.stop()
        self.tts.startSpeakingString_(str(text))

    def stop(self):
        '''Halts any current speech events'''
        self.tts.stopSpeaking()

    def available_voices(self):
        '''Returns a list of voices available for use with NSSS'''
        voices = NSSpeechSynthesizer.availableVoices()
        voices = list(voices)
        for x in voices:
            x.encode()
        return voices

    def get(self,attribute):
        '''Returns the specified attribute

        Recognized attributes: rate, voice, volume'''
        attribute = attribute.lower()
        if attribute == "voice":
            return self.tts.voice().encode("ascii").split(".")[-1]
        elif attribute == "volume":
            return self.tts.volume()*100
        elif attribute == "rate":
            return self.tts.rate()
        else:
            raise ValueError("\"%s\" not a recognized attribute" % (attribute))

    def set(self, attribute, value):
        '''Sets the specified attribute to the given value

        Recognized attributes: rate, voice, volume'''
        attribute = attribute.lower()
        if attribute == "voice":
            if not isinstance(value,str):
                raise TypeError("voice must be of type \"string\"")
            elif value not in self.available_voices():
                raise ValueError("%s is not an available voice" % (value))
            else:
                lss = NSSpeechSynthesizer.availableVoices()
                for ii in lss:
                    if ii.split(".")[-1] == value:
                        value = ii
                        break
                vol = self.tts.volume()
                rate = self.tts.rate()
                self.tts.setVoice_(value)
                self.tts.setRate_(rate)
                self.tts.setVolume_(vol)
        elif attribute == 'rate':
            if not isinstance(value,(int,float)):
                raise TypeError("volume must be either an integer or floating point number")
            elif not 50 <= value <= 600:
                raise ValueError("volume value must be in range 50--600")
            else:
                self.tts.setRate_(value)
        elif attribute == 'volume':
            if not isinstance(value,(int,float)):
                raise TypeError("volume must be either an integer or floating point number")
            elif not 0 <= value <= 100:
                raise ValueError("volume value must be in range 0--100")
            else:
                self.tts.setVolume_(value*0.01)
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
        tempproc = subprocess.Popen(["say","-v",self.tts.voice().encode("ascii").split(".")[-1],"-o",path[:-4],"--data-format=LEF32@8000","--file-format=WAVE","\""+text+"\""])