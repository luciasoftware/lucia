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
And in addition
* docs - documentation for lucia (auto generated)
* tests - tests for lucia.

### Building / Running:
#### Running tests:
To run the tests run the following command:
> $ python setup.py test

#### Generating documentation:
To generate Lucia's documentation, you first need to install Sphinx
 > $ pip install Sphinx
 after to into the "docs" folder and run:
 > $ cd docs
 > $ ./make.bat

### Contributing
Everyone is welcome to help improve Lucia, to start look at the opened issues, and go from there.

### License:
Copyright (C) 2019  LuciaSoftware and it's contributors.
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, version 3 of the License.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.
You should have received a copy of the GNU Lesser General Public License
along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.
