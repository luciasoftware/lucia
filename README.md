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
* lucia/utils - things coded into the engine, but not necessarily required in every game.
And in addition
* docs - documentation for lucia (auto generated)
* examples - Examples that showcases different things that can be done with lucia.
* web - The advanced documentation and use cases for lucia.
* tests - tests for lucia.


### Installing lucia
There's the to default ways to install lucia.
Through pip

```
pip install lucia
```

Or the manual way

```
git clone https://github.com/LuciaSoftware/lucia.git
cd lucia
python setup.py install
```


### Building / Running:
#### Running tests:
To run the tests run the following command:
```
python setup.py test
```

#### Generating documentation:
To generate Lucia's documentation, you first need to install Sphinx

```
pip install Sphinx
```

after go into the "docs" folder:
```
cd docs
```

And run:
```
./make.bat
```


#### Generating the advanced documentation and use cases (web):
To generate the web documentation (the one found in "web") you first need to install mkdocs.

```
pip install mkdocs
```

after go into the "web" folder:

```
cd web
```

And run:

```
mkdocs build
```


Alternatively, you can also view a local demo of the docs by executing the following command:

```
mkdocs serve
```


### Contributing
Everyone is welcome to help improve Lucia, to start look at the opened issues, and go from there.
If you feel lucia is missing something, do open an issue and we'll take it from there.


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
