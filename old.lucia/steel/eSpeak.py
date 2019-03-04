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
# file:          eSpeak.py
# purpose:       Provides a wrapper for the eSpeak text-to-speech engine
# classes:       eSpeak
# functions:
#
# To do: Add support for Mbrola voices
#

import platform
import os
import subprocess

class eSpeak():
    '''eSpeak Speech Synthesizer wrapper'''
    def __init__(self):
        if platform.system() == "Windows":
            for path in [os.environ.get('ProgramFiles'),os.environ.get('ProgramFiles(86)',None),os.environ.get('ProgramW6432',None)]:
                if path != None and os.path.isdir(path+"/eSpeak"):
                    self.pathstr = path+"/eSpeak/command_line/eSpeak"
                    self.data = path+"/eSpeak/espeak_data"
        else:
            if os.path.isdir("/usr/share/espeak-data"):
                self.pathstr = "espeak"
                self.data = "/usr/share/espeak-data"
            elif os.path.isdir(os.path.expanduser("~/espeak-data")):
                self.pathstr = "espeak"
                self.data = os.path.expanduser("~/espeak-data")
        if not hasattr(self,'data'):
            raise RuntimeError("eSpeak not properly installed on this computer")
        self.pathstr = self.pathstr.replace("\\","/")
        self.data = self.data.replace("\\","/")

        self.volume = 50
        self.pitch = 50
        self.rate = 200
        self.voice = "default"
        self.variant = ""

    def speak(self, text, interrupt=False):
        '''Speaks the given string of text'''
        if not isinstance(text, str):
            raise TypeError("Text must be of type \"string\"")
        elif interrupt:
            self.stop()
        if platform.system() == "Windows":
            self.proc = subprocess.Popen("%s -s %s -p %s -a %s -z -v%s%s \"%s\"" % (self.pathstr, int(self.rate), int(self.pitch), int(self.volume*2), self.voice, self.variant, text))
        else:
            self.proc = subprocess.Popen([self.pathstr,"-s",str(int(self.rate)),"-p",str(int(self.pitch)),"-a",str(int(self.volume*2)),"-z","-v"+self.voice+self.variant,"\""+text+"\""])

    def stop(self):
        '''Halts any current speech events'''
        if getattr(self,'proc',None) != None:
            self.proc.terminate()

    def available_voices(self):
        '''Returns a list of voices available for use with eSpeak'''
        files = [f.split('.')[0] for f in os.listdir(self.data+"/voices") if os.path.isfile(os.path.join(self.data+"/voices",f))]
        files += [f.split('.')[0] for f in os.listdir(self.data+"/asia") if os.path.isfile(os.path.join(self.data+"/asia",f))]
        files += [f.split('.')[0] for f in os.listdir(self.data+"/europe") if os.path.isfile(os.path.join(self.data+"/europe",f))]
        files += [f.split('.')[0] for f in os.listdir(self.data+"/mb") if os.path.isfile(os.path.join(self.data+"/mb",f))]
        files += [f.split('.')[0] for f in os.listdir(self.data+"/other") if os.path.isfile(os.path.join(self.data+"/other",f))]
        files += [f.split('.')[0] for f in os.listdir(self.data+"/test") if os.path.isfile(os.path.join(self.data+"/test",f))]
        return files

    def available_variants(self):
        '''Returns a list of variants available for use with eSpeak'''
        files = [f.split('.')[0] for f in os.listdir(self.data+"/voices/!v") if os.path.isfile(os.path.join(self.data+"/voices/!v",f))]
        return files

    def get(self, attribute):
        '''Returns the specified attribute

        Recognized attributes: pitch, rate, variant, voice, volume'''
        attribute = attribute.lower()
        if attribute == "pitch":
            return self.pitch
        elif attribute == "rate":
            return self.rate
        elif attribute == "variant":
            return self.variant[1:]
        elif attribute == "voice":
            return self.voice
        elif attribute == "volume":
            return self.volume
        else:
            raise ValueError("\"%s\" not a recognized attribute" % (attribute))

    def set(self, attribute, value):
        '''Sets the specified attribute to the given value

        Recognized attributes: pitch, rate, variant, voice, volume'''
        attribute = attribute.lower()
        if attribute in ["rate","volume","pitch"]:
            if not isinstance(value,(int,float)):
                raise TypeError("%s must be either an integer or floating point number" % (attribute))
            elif attribute in ["volume","pitch"] and not 0 <= value <= 100:
                raise ValueError("%s value must be in range 0--100" % (attribute))
            elif attribute == "rate" and not 80 <= value <= 450:
                raise ValueError("rate value must be in range 80--450")
            else:
                exec("self.%s = int(round(float(value),0))" % (attribute))
        elif attribute in ["voice","variant"]:
            if not isinstance(value,str):
                raise TypeError("%s must be of type \"string\"" % (attribute))
            elif attribute == "voice":
                if value not in self.available_voices():
                    raise ValueError("%s is not an available voice" % (value))
                else:
                    self.voice = value
            elif attribute == "variant":
                if value not in self.available_variants():
                    raise ValueError("%s is not an available variant" % (value))
                else:
                    self.variant = "+" + value
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
            if platform.system() == "Windows":
                tempproc = subprocess.Popen("%s -s %s -p %s -a %s -z -v%s%s -w \"%s\" \"%s\"" % (self.pathstr, int(self.rate), int(self.pitch), int(self.volume*2), self.voice, self.variant, path, text))
            else:
                tempproc = subprocess.Popen([self.pathstr,"-s",str(int(self.rate)),"-p",str(int(self.pitch)),"-a",str(int(self.volume*2)),"-z","-v"+self.voice+self.variant,"-w","\""+path+"\"","\""+text+"\""])
