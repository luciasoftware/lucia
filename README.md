# lucia

[![Build Status](https://travis-ci.com/luciasoftware/lucia.svg?branch=master)](https://travis-ci.com/luciasoftware/lucia)

# [INSTALLATION](https://LuciaSoftware.github.io/lucia#Installation) | [DOCUMENTATION](https://LuciaSoftware.github.io/lucia) | [LICENSE](https://github.com/LuciaSoftware/lucia/blob/master/LICENSE)

### An audio game engine written in python

### Goals:
The goal of lucia is to change the audio game creation method from the now old and no longer maintained bgt, to python.
Lucia should not act as a starting game, but as a base, that a high quality game can be build upon.
In addition lucia should be cross platform, At Least on windows and mac.
> Code / dependencies that doesn't meet these requirements cannot be a part of lucia.

### Installation
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
To generate Lucia's documentation, you first need to install pydoc-markdown

```
pip install pydoc-markdown
```

after go into the "docs" folder:
```
cd docs
```

And run:
```
pydocmd build
```


Alternatively, you can also view a local demo of the docs by executing the following command:

```
pydocmd serve
```


### Contributing

Everyone is welcome to help improve Lucia. start [here](https://github.com/luciasoftware/lucia/blob/master/contributing.md)



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
