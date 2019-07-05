"""tests lucias data module"""
from lucia import data


def test_compression():
	original = b"This is a string, that will be changed in many ways."

	compressed = data.compress(original)
	assert compressed is not None
	assert compressed is not original
	decompressed = data.decompress(compressed)
	assert original == decompressed


def test_encryption():
	original = b"This is a plain string, that will be encrypted and then decrypted - let's see how it goes."
	key = "ThisIsMyVerySecretKey123456789"

	encrypted = data.encrypt(original, key)
	decrypted = data.decrypt(encrypted, key)

	assert original == decrypted
