# lucia
An audio game engine written in python

### Goals:
The goal of lucia is to change the audio game creation method from the now old and no longer maintained bgt, to python.
Lucia should not act as a starting game, but as a base, that a high quality game can be build upon.
In addition lucia should be cross platform, At Least on windows and mac.
> Code / dependencies that doesn't meet these requirements cannot be a part of lucia.

### Folder explenations:
* Lucia - the main lucia engine.
* lucia/audio - Audio handling.
* lucia/interface - things that pop onto the screen (like menus, edit fields and dialogs).
* lucia/utils - things coded into the engine, but not necessarily required in any game.

### Todo
* Add checksum checks to the resource manager.
* Proper distance handling with rolloff and silence after a certain distance, should be no more than 70.
* A documentation of the toolset available and how it may be used, with some examples.
* More exceptions need to be thrown out to the user (for better error handling).

# Bugs (issues can be attached)
* Resource files doesn't load correctly on mac.
* There exists a bug, that shws after installing lucia (ImportError, no module named pywintypes). For now, a fix is by reinstalling pywin32 (pip uinstall pywin32 and pip install pywin32).
