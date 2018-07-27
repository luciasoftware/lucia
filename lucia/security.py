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

# Changes this for more security
# Note: If you change this, please note that it must be 16 characters long.
iv = "0000000000000000"

# Compression preset (default 6, between 1-9).
compression_level = 6

import lzma
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA1
from Cryptodome.Hash import SHA256

# Internal functions.
def encrypt_data(key, data):
	try:
		key = key.encode("utf-8")
	except AttributeError:
		pass
	try:
		data = data.encode("utf-8")
	except AttributeError:
		pass
	encryptor = AES.new(SHA256.new(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	return encryptor.encrypt(data)


def decrypt_data(key, data):
	try:
			key = key.encode("utf-8")
	except AttributeError:
		pass
	decryptor = AES.new(SHA256.new(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	decryptedData = decryptor.decrypt(data)
	return decryptedData

def compress_data(data):
	return lzma.compress(data, preset=compression_level)

def decompress_data(data):
	return lzma.decompress(data)

