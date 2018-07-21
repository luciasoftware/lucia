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
# file:          FreeTTS.py
# purpose:       Provides a wrapper for the FreeTTS text-to-speech engine
# classes:       FreeTTS
# functions:     None
#

import platform
import os
import subprocess

class FreeTTS():
    '''FreeTTS speech synthesis wrapper'''
    def __init__(self):
        if os.system("java -version") != 0:
            raise RuntimeError("Java not properly installed on this computer")
        if platform.system() == "Windows":
            for path in [os.environ.get('ProgramFiles'),os.environ.get('ProgramFiles(86)',None),os.environ.get('ProgramW6432',None)]:
                if path != None and os.path.isdir(path+"/freetts"):
                    self.path = path+"/freetts/lib/freetts.jar"
        elif platform.system()[:3] == "CYG":
            #---Account for when Cygwin is using Windows installation of FreeTTS or Java---#
            rtt = subprocess.Popen(["whereis","java"],stdout=subprocess.PIPE)
            if rtt.stdout.read()[:15] == "java: /cygdrive":
                if os.path.isdir("c:/Program Files/freetts"):
                    self.path = "c:/Program Files/freetts/lib/freetts.jar"
                elif os.path.isdir("c:/Program Files (x86)/freetts"):
                    self.path = "c:/Program Files (x86)/freetts/lib/freetts.jar"
                elif os.path.isdir("c:/cygwin/usr/share/freetts"):
                    self.path = "c:/cygwin/usr/share/freetts/lib/freetts.jar"
                elif os.path.isdir("c:/cygwin/%s" % os.path.expanduser("~/freetts")):
                    self.path = "c:/cygwin/%s" % os.path.expanduser("~/freetts/lib/freetts.jar")
            else:
                if os.path.isdir("/cygdrive/c/Program Files/freetts"):
                    self.path = "/cygdrive/c/Program Files/freetts/lib/freetts.jar"
                elif os.path.isdir("/cygdrive/c/Program Files (x86)/freetts"):
                    self.path = "/cygdrive/c/Program Files (x86)/freetts/lib/freetts.jar"
                elif os.path.isdir("/usr/share/freetts"):
                    self.path = "/usr/share/freetts/lib/freetts.jar"
                elif os.path.isdir(os.path.expanduser("~/freetts")):
                    self.path = os.path.expanduser("~/freetts/lib/freetts.jar")
        else:
            if os.path.isdir("/usr/share/freetts"):
                self.path = "/usr/share/freetts/lib/freetts.jar"
            elif os.path.isdir(os.path.expanduser("~/freetts")):
                self.path = os.path.expanduser("~/freetts/lib/freetts.jar")
        if not hasattr(self,'path'):
            raise RuntimeError("FreeTTS not properly installed on this computer")
        if platform.system() == "Windows":
            self.proc = subprocess.Popen("java -jar \"%s\" -streaming"%(self.path),stdin=subprocess.PIPE)
        else:
            self.proc = subprocess.Popen(["java","-jar",self.path,"-streaming"],stdin=subprocess.PIPE)
        self.voice = "kevin16"

    def speak(self,text,interrupt=False):
        '''Speaks the given string of text'''
        if not isinstance(text, str):
            raise TypeError("Text must be of type \"string\"")
        if interrupt:
            self.stop()
        self.proc.stdin.write(text+"\n")

    def stop(self):
        '''Halts any current speech events'''
        self.proc.terminate()
        if platform.system() == "Windows":
            self.proc = subprocess.Popen("java -jar \"%s\" -streaming -voice %s" % (self.path,self.voice),stdin=subprocess.PIPE)
        else:
            self.proc = subprocess.Popen(["java","-jar",self.path,"-streaming","-voice",self.voice],stdin=subprocess.PIPE)

    def available_voices(self):
        '''Returns a list of voices available for use with FreeTTS'''
        if platform.system() == "Windows":
            a = subprocess.Popen("java -jar \"%s\" -voiceInfo"%(self.path),stdout=subprocess.PIPE)
        else:
            a = subprocess.Popen(["java","-jar",self.path,"-voiceInfo"],stdout=subprocess.PIPE)
        list1 = a.communicate()[0].split("Name: ")[1:]
        voices = []
        for ii in list1:
            voices.append(ii.split("\r\n")[0])
        return voices

    def get(self, attribute):
        '''Returns the specified attribute

        Recognized attributes: voice'''
        attribute = attribute.lower()
        if attribute == "voice":
            return self.voice
        else:
            raise ValueError("\"%s\" not a recognized attribute" % (attribute))

    def set(self, attribute, value):
        '''Sets the specified attribute to the given value

        Recognized attributes: voice'''
        # To do: Handle pitch/rate/volume
        attribute = attribute.lower()
        if attribute == "voice":
            if not isinstance(value,str):
                raise TypeError("voice must be of type \"string\"")
            elif value not in self.available_voices():
                raise ValueError("%s is not an available voice" % (value))
            else:
                self.voice = value
                self.proc.terminate()
                if platform.system() == "Windows":
                    self.proc = subprocess.Popen("java -jar \"%s\" -streaming -voice %s" % (self.path,self.voice),stdin=subprocess.PIPE)
                else:
                    self.proc = subprocess.Popen(["java","-jar",self.path,"-streaming","-voice",self.voice],stdin=subprocess.PIPE)
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
                tempproc = subprocess.Popen("java -jar \"%s\" -streaming -voice %s -dumpAudio %s -text %s" % (self.path,self.voice, path, text))
            else:
                tempproc = subprocess.Popen(["java","-jar",self.path,"-streaming","-voice",self.voice,"-dumpAudio",path,"-text",text])
