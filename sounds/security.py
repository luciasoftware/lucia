# Changes this for more security
# Note: If you change this, please note that it must be 16 characters long.
iv = "0000000000000000"

# Compression preset (default 6, between 1-9).
compression_level = 6

import hashlib, lzma
from Cryptodome.Cipher import AES

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
	encryptor = AES.new(hashlib.sha256(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	return encryptor.encrypt(data)


def decrypt_data(key, data):
	try:
			key = key.encode("utf-8")
	except AttributeError:
		pass
	decryptor = AES.new(hashlib.sha256(key).digest(), AES.MODE_CFB, iv.encode("utf-8"))
	decryptedData = decryptor.decrypt(data)
	return decryptedData

def compress_data(data):
	return lzma.compress(data, preset=compression_level)

def decompress_data(data):
	return lzma.decompress(data)

