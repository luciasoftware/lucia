# Note: this setup file isn't made to publish on pypi yet
# Note: To make it ready for official publishing, continue guide at: https://python-packaging.readthedocs.io/en/latest/metadata.html
# Note2: When adding extra dependencies to lucia, remember to add them below (and their source link, if they aren't available on pypi).

from setuptools import setup

def readme():
	with open('README.md') as f:
		return f.read()

dependencies =[
'pysdl2',
'pycryptodomex',
'pysoundfile',
'numpy',
'bson',
'PyAl',
'platform_utils',
'libloader',
'sound_lib',
'accessible_output2',
]

setup(
name='lucia',
version='0.0.1',
description='A cross platform, feature rich audio game engine written in Python.',
long_description=readme(),
url='http://github.com/LuciaSoftware/lucia',
author='Lucia Software',
license='LGPL',
packages=['lucia', 'lucia.audio', 'lucia.audio.bass', 'lucia.audio.openal', 'lucia.ui', 'lucia.utils'],
setup_requires=["pytest-runner"],
tests_require=["pytest"] + dependencies,
install_requires=dependencies,
    dependency_links=[
'https://github.com/NicklasMCHD/PyAL/tarball/master#egg=PyAL',
'https://github.com/Accessiware/platform_utils/tarball/master#egg=platform_utils',
'https://github.com/Accessiware/libloader/tarball/master#egg=libloader',
'https://github.com/Accessiware/sound_lib/tarball/master#egg=sound_lib',
'https://github.com/Accessiware/accessible_output2/tarball/master#egg=accessible_output2',
],
include_package_data=True,
package_data={'lucia': ['OpenAL32.dll', 'SDL2.dll']},
zip_safe=False
)
