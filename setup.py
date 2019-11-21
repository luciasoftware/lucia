from setuptools import setup, find_packages
import platform
import versioneer
 
def readme():
	with open('README.md') as f:
		return f.read()

dependencies =[
'pygame',
'pycryptodomex',
'pysoundfile',
'numpy',
'sound_lib',
'pyal',
'accessible_output2',
'bson',
'versioneer',
]

if platform.system() == "Darwin":
	dependencies.append("appscript")

if platform.system() == "Windows":
	dependencies.append("pywin32")
	dependencies.append("pypiwin32")

lucia_packages = find_packages(".")


setup(
name='lucia',
version=versioneer.get_version(),
cmdclass=versioneer.get_cmdclass(),
description='A cross platform, feature rich audio game engine written in Python.',
long_description=readme(),
long_description_content_type="text/markdown",
url='http://github.com/LuciaSoftware/lucia',
keywords=("audiogame bgt lucia python python3 luciasoftware"),
author='Lucia Software',
license='LGPL',
packages=lucia_packages,
entry_points="""
[console_scripts]
lucia.packer=lucia.cli.packer:main
lucia=lucia.cli:main
""",
setup_requires=["pytest-runner"],
tests_require=["pytest"] + dependencies,
install_requires=dependencies,
    dependency_links=[
'https://github.com/NicklasMCHD/PyAL/tarball/master#egg=PyAL',
'https://github.com/accessiware/platform_utils/tarball/master#egg=platform_utils',
'https://github.com/accessiware/libloader/tarball/master#egg=libloader',
],
include_package_data=True,
zip_safe=False,
classifiers=[
"Development Status :: 4 - Beta",
'Environment :: MacOS X',
'Environment :: Win32 (MS Windows)',
"Environment :: Console",
"Intended Audience :: Developers",
"License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
'Topic :: Games/Entertainment',
'Topic :: Software Development :: Libraries :: Python Modules',
'Operating System :: MacOS :: MacOS X',
'Operating System :: Microsoft :: Windows',
"Programming Language :: Python :: 3.4",
"Programming Language :: Python :: 3.5",
"Programming Language :: Python :: 3.6",
"Programming Language :: Python :: 3.7",
],
)
