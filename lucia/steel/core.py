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
# file:          core.py
# purpose:       Defines general utility functions
# classes:       None
# functions:     available_engines()
#                play_wav()
#

import platform
import os

if platform.system() == "Windows":
    import winreg

def available_engines():
    '''Returns a list of available TTS software installed on computer
    Returns [] if none available

    Possible values: 'eSpeak', 'SAPI5', 'NSSS', 'FreeTTS'
    '''
    available = []

    #---Check for Microsoft Speech API 5.x---#
    if platform.system() == "Windows":
        try:
            winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, "SAPI.SPVoice")
            available.append("SAPI5")
        except:
            pass

    #---Check for NS Speech Synthesizer---#
    if platform.system() == "Darwin":
        try:
            from AppKit import NSSpeechSynthesizer
            available.append("NSSS")
        except ImportError:
            try:
                from Cocoa import NSSpeechSynthesizer
                available.append("NSSS")
            except:
                pass

    #---Check for eSpeak---#
    if platform.system() == "Windows":
        for path in [os.environ.get('ProgramFiles'),os.environ.get('ProgramFiles(86)',None),os.environ.get('ProgramW6432',None)]:
            if path != None and os.path.isdir(path+"/eSpeak"):
                available.append("eSpeak")
    else:
        if os.path.isdir("/usr/share/espeak-data") or os.path.isdir(os.path.join(os.path.expanduser("~/"),"espeak-data")):
            available.append("eSpeak")

    #---Check for FreeTTS---#
    if os.system("java -version") == 0:
        if platform.system() == "Windows":
            for path in [os.environ.get('ProgramFiles'),os.environ.get('ProgramFiles(86)',None),os.environ.get('ProgramW6432',None)]:
                if path != None and os.path.isdir(path+"/freetts"):
                    available.append("FreeTTS")
        elif platform.system()[:3] == "CYG":
            if os.path.isdir("/cygdrive/c/Program Files/freetts") or os.path.isdir("/cygdrive/c/Program Files (x86)/freetts") or os.path.isdir("/usr/share/freetts") or os.path.isdir(os.path.expanduser("~/freetts")):
                available.append("FreeTTS")
        else:
            if os.path.isdir("/usr/share/freetts") or os.path.isdir(os.path.expanduser("~/freetts")):
                available.append("FreeTTS")
    return available

def play_wav(path):
    '''Plays the .wav file at the specified path'''
    if not isinstance(path, str):
        raise TypeError("Path must be of type \"string\"")
    elif path[-4:] != ".wav":
        raise ValueError("Path must specify a .wav file")
    path = os.path.expandvars(os.path.expanduser(path))
    if not os.path.isfile(path):
        raise ValueError("Path must specify a valid .wav file")
    elif platform.system() == "Windows":
        import winsound
        winsound.PlaySound(path,winsound.SND_FILENAME|winsound.SND_ASYNC)
    elif platform.system() == "Darwin":
        import subprocess
        tempproc = subprocess.Popen(["afplay",path])
    else:
        import subprocess
        if os.path.isfile("/usr/bin/mplayer"): #mplayer
            tempproc = subprocess.Popen(["mplayer",path])
        elif os.path.isfile("/usr/bin/play"): #sox
            tempproc = subprocess.Popen(["play",path])
        else:
            raise RuntimeError("Compatible audio player not installed")
