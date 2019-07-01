# Copyright (C) 2018  LuciaSoftware and it's contributors.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see https://github.com/LuciaSoftware/lucia/blob/master/LICENSE.

"""Provides functions for easily manipulating textual or binary data.
Currently includes encryption and compression.
"""

import lzma
import zlib
import bz2
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA256
from Cryptodome.Util.Padding import *
from Cryptodome import Random

#constants
#compression
ZLIB = 1
LZMA = 2
BZ2=3

class unsupportedAlgorithm(Exception):
	"""raised when the user tries supplying an algorithm not specified in constants"""
	pass

def encrypt(data, key):
	try:
		key = key.encode("utf-8")
	except AttributeError:
		pass
	try:
		data = data.encode("utf-8")
	except AttributeError:
		pass
	iv = Random.new().read(AES.block_size)
	#Hashing key with SHA256 entirely alleviates the need for any padding.
	key = SHA256.new(key).digest()
	#len(data) must be a factor of AES.block_size.
	data = pad(data, AES.block_size)
	encryptor = AES.new(key, AES.MODE_CFB, iv)
	return encryptor.encrypt(data)+iv

def decrypt(data, key):
	try:
			key = key.encode("utf-8")
	except AttributeError:
		pass
	#Hashing key with SHA256 entirely alleviates the need for any padding.
	key = SHA256.new(key).digest()
	iv = data[-AES.block_size:]
	data = data[:AES.block_size]
	decryptor = AES.new(key, AES.MODE_CFB, iv)
	decryptedData = decryptor.decrypt(data)
	return unpad(decryptedData, AES.block_size)

def compress(data, algorithm=ZLIB, compression_level=6):
	if not isinstance(data, bytes):
		data=data.encode()
	if algorithm==ZLIB:
		return zlib.compress(data, level=compression_level)
	elif algorithm==LZMA:
		return lzma.compress(data, preset=compression_level)
	elif algorithm == BZ2:
		return bz2.compress(data, compresslevel=compression_level)
	else:
		raise unsupportedAlgorithm

def decompress(data, algorithm=ZLIB):
	if not isinstance(data, bytes):
		data=data.encode()
	if algorithm==ZLIB:
		return zlib.decompress(data)
	elif algorithm==LZMA:
		return lzma.decompress(data)
	elif algorithm == BZ2:
		return bz2.decompress(data)
	else:
		raise unsupportedAlgorithm
