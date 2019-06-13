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

#constants
#compression
ZLIB = 1
LZMA = 2
BZ2 = 3
import lzma
import zlib
import bz2
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA1
from Cryptodome.Hash import SHA256
import pickle, sys, os, struct, base64

class ResourceFileVersion:
	"""The version should only change, if changes are introduced, that breaks backward compatibility"""
	v1 = 1

class ResourceFileItem(object):
	def __init__(self, name, content, compress, encrypt):
		self.name = name
		self.content = content
		self.compress = compress
		self.encrypt = encrypt

class ResourceFile:
	def __init__(self, key, iv="1010102010101020", header="lucia", version=ResourceFileVersion.v1):
		self.key = key
		self.iv = iv
		self.header = header
		if isinstance(self.header, str):
			self.header = self.header.encode()
		self.header_length = len(self.header)
		self.version = version
		self.files = {}

	def load(self, filename):
		f = open(filename, "rb")
		test_header = f.read(self.header_length)
		test_header = struct.unpack(str(self.header_length)+"s", test_header)[0]
		test_version = f.read(4)
		test_version = struct.unpack("1i", test_version)[0]
		amount_of_files = f.read(4)
		amount_of_files = struct.unpack("1i", amount_of_files)[0]
		if test_header != self.header:
			raise InvalidPackHeader
		if test_version != self.version:
			raise InvalidPackHeader
		if amount_of_files == 0:
			raise InvalidPackHeader
		# Header and version is good, nice. Now resolve files.
		for x in range(0, amount_of_files):
			name_length = struct.unpack("1i", f.read(4))[0]
			name = f.read(name_length)
			content_length = struct.unpack("1i", f.read(4))[0]
			content_state = struct.unpack("2i", f.read(8))
			content = f.read(content_length)
			if content_state[1]:
				content = decrypt_data(content, self.key, self.iv)
			if content_state[0]:
				content = decompress_data(content)
			item = ResourceFileItem(name, content, content_state[0], content_state[1])
			self.files[name] = item

	def save(self, filename):
		f = open(filename, "wb")
	# first write header
		f.write(struct.pack(str(self.header_length)+"s", self.header))
		# then write the version byte
		f.write(struct.pack("1i", self.version))
		# Write how many files are in the pack
		f.write(struct.pack("1i", len(self.files)))
		# and then loop through all files, and add them to the pack.
		for item in self.files.values():
			f.write(struct.pack("1i", len(item.name)))
			f.write(item.name)
			content = item.content
			if item.compress:
				content = compress_data(item.content)
			if item.encrypt:
				content = encrypt_data(content, self.key, self.iv)
			f.write(struct.pack("1i", len(content)))
			f.write(struct.pack("2i", item.compress, item.encrypt))
			f.write(content)
		# and then close
		f.close()

	def add_file(self, name, compress=True, encrypt=True, internalname=None, ):
		if os.path.exists(name) == False:
			raise FileNotFoundError
		f = open(name, "rb")
		content = f.read()
		f.close()
		if internalname is not None:
			name = internalname
		if isinstance(name, str):
			name = name.encode()
		item = ResourceFileItem(name, content, compress, encrypt)
		self.files[name] = item

	def add_memory(self, name, content, compress=True, encrypt=True):
		if isinstance(name,str):
			name = name.encode()
		if isinstance(content,str):
			content = content.encode()
		item = ResourceFileItem(name, content, compress, encrypt)
		self.files[name] = item

	def get(self, name):
		if isinstance(name, str):
			name = name.encode()
		val = self.files[name]
		if isinstance(val,ResourceFileItem):
			return val.content
		return None

	def exist(self, name):
		if isinstance(name, str):
			name = name.encode()
		return name in self.files.keys()

	def list(self):
		return self.files.keys()


# Internal stuff.
class unsupportedAlgorithm(Exception):
	"""raised when the user tries supplying an algorithm not specified in constants"""
	pass

class InvalidPackHeader(Exception):
	"""raised when the packs header is invalid"""
	pass

class InvalidInitializationVector(Exception):
	"""raised if the initialization vector, given to the encryption or decryption methods aren't 16 bytes long"""
	pass


def encrypt_data(data, key, iv):
	if len(iv) != 16:
		raise InvalidInitializationVector
		return
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

def decrypt_data(data, key,iv):
	if len(iv) != 16:
		raise InvalidInitializationVector
		return
	try:
			key = key.encode("utf-8")
	except AttributeError:
		pass
	decryptor = AES.new(SHA256.new(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	decryptedData = decryptor.decrypt(data)
	return decryptedData

def compress_data(data, algorithm=1, compression_level=6):
	if type(data)!=bytes:
		data=data.encode()
	if algorithm==1:
		return zlib.compress(data, level=compression_level)
	elif algorithm==2:
		return lzma.compress(data, preset=compression_level)
	elif algorithm == 3:
		return bz2.compress(data, compresslevel=compression_level)
	else:
		raise unsupportedAlgorithm

def decompress_data(data, algorithm=1):
	if type(data)!=bytes:
		data=data.encode()
	if algorithm==1:
		return zlib.decompress(data)
	elif algorithm==2:
		return lzma.decompress(data)
	elif algorithm == 3:
		return bz2.decompress(data)
	else:
		raise unsupportedAlgorithm
