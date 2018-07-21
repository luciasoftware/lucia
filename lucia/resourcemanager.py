# These are the file types you want to exclude from the pack.
excluded_file_types = (".py", ".pyc", ".log", ".dll", ".dat")


import pickle, sys, os
from .security import *

class ResourceManager():
	def __init__(self):
		self.data = {}

	def load_resources(self, file, password):
		f = open(file, "rb")
		eD = f.read()
		f.close()
		qData = decrypt_data(password, eD)
		sData = pickle.loads(qData)
		tmpData = {}
		for key in sData:
			tmpData[key] = decompress_data(sData[key])
		self.data.update(tmpData)

	def get_resource(self, k):
		result = self.data[k]
		return result

	# short hand function
	def get(self, k):
		return self.get_resource(k)

	def set_resource(self, k, v):
		self.data[k] = v

	# short hand function
	def set(self, k, v):
		self.set_resource(k, v)

	def save_resources(self, file, password):
		saveData = self.data
		for key in saveData:
			saveData[key] = compress_data(saveData[key])
		tmpData = pickle.dumps(saveData)
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
	
	storedFiles = {}
	key = pwd
	
	print("Reading files from system. Please wait!")
	for path, subdirs, files in os.walk(os.getcwd()):
		for name in files:
			p = os.path.join(path, name)
			niceName = p[1+len(os.getcwd()):].replace("\\", "/")
			if niceName.lower().endswith(excluded_file_types):
				print("Skipping " + niceName + ".")
				continue
			print("Compressing " + niceName + ".")
			f = open(p, "rb")
			data = f.read()
			f.close()
			storedFiles[niceName] = compress_data(data)
			del data
	
	print("Converting data.")
	tmpData = pickle.dumps(storedFiles)
	print("Encrypting data...")
	encryptedData = encrypt_data(key, tmpData)
	print("Writing data to disk...")
	f = open(resourceFile, "wb")
	f.write(	encryptedData)
	f.close()
	print("Done")
	print("Running checks on generated resources file.")
	f = open(resourceFile, "rb")
	eD = f.read()
	f.close()
	qData = decrypt_data(key, eD)
	sData = pickle.loads(qData)
	print("Running decryption/decompression test.")
	testData = {}
	for key in sData:
		testData[key] = decompress_data(sData[key])
	print("decryption/decompression test passed.")
	print("Running byte matcher test.")
	if len(testData) == len(storedFiles):
		print("Passed byte matcher.")
	else:
		print("Warning: Bytematching failed. This can happen if you have non-audio files in your resources file.")
	print("Done")
