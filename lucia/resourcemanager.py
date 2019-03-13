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

# These are the file types you want to exclude from the pack.
excluded_file_types = (".py", ".pyc", ".log", ".dll", ".dat")

class unsupportedAlgorithm(Exception):
	"""raised when the user tries supplying an algorithm not specified in constants"""
	pass

# Changes this for more security
# Note: If you change this, please note that it must be 16 characters long.
iv = "0000000000000000"


import lzma
import zlib
import bz2
from Cryptodome.Cipher import AES
from Cryptodome.Hash import SHA1
from Cryptodome.Hash import SHA256
import pickle, sys, os

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

class ResourceManager():
	def __init__(self):
		self.data = {}

	def load(self, file, password):
		f = open(file, "rb")
		eD = f.read()
		f.close()
		if len(eD) <= 0:
			return
		qData = decrypt_data(password, eD)
		sData = decompress_data(qData)
		cData = pickle.loads(sData)
		self.data.update(cData)

	def create_and_load(self, filename, password):
		if os.path.isfile(filename):
			return self.load(filename, password)
		else:
			f = open(filename, "w")
			f.close()
			return self.load(filename, password)

	def get_resource(self, k):
		result = self.data[k]
		if self.data[k+".hash"] != SHA1.new(result).digest():
			raise ValueError(f"checksum validation failed for item {k}.")
			return None
		return result

	# short hand function
	def get(self, k):
		return self.get_resource(k)

	def set_resource(self, k, v):
		self.data[k] = v
		self.data[k+".hash"] = SHA1.new(v).digest()

	# short hand function
	def set(self, k, v):
		self.set_resource(k, v)

	def save(self, file, password):
		saveData = self.data
		tmpData = pickle.dumps(saveData)
		tmpData = compress_data(tmpData)
		encryptedData = encrypt_data(password, tmpData)
		f = open(file, "wb")
		f.write(	encryptedData)
		f.close()


if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("Usage: " + sys.argv[0] + " key")
		print("Usage: " + sys.argv[0] + " key file")
		print("")
		print("key - required - encryption key to use.")
		print("file - optional - The filename to write the encrypted data to (default \"resources.dat\")")
		sys.exit()
	
	pwd = sys.argv[1]
	resourceFile = "resources.dat"
	if len(sys.argv) == 3:
		resourceFile = sys.argv[2]
	
	print("Starting")
	print("Key: " + pwd)
	print("Resource File: " + resourceFile)
	print("")
	
	key = pwd
	
	ress = ResourceManager()
	print("Reading files from system. Please wait!")
	for path, subdirs, files in os.walk(os.getcwd()):
		for name in files:
			p = os.path.join(path, name)
			niceName = p[1+len(os.getcwd()):].replace("\\", "/")
			if niceName.lower().endswith(excluded_file_types):
				print("Skipping " + niceName + ".")
				continue
			print("Adding " + niceName + ", ", end="")
			f = open(p, "rb")
			data = f.read()
			f.close()
			ress.set(niceName, data)
			del data
			print("done.")
	
	print("Saving data, ", end="")
	ress.save(resourceFile, key)
	print("Done")
