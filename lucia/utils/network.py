import struct
import base64
import bson

# socket send all and read all functions
def send_message(sock, encryptor_function, msg):
	if isinstance(msg, dict) == False:
		raise ValueError("supplied message is not of type dict")
		return
	msg = bson.dumps(msg)
	msg = encryptor_function(msg)
	# Prefix each message with a 4-byte length (network byte order)
	msg = struct.pack('>I', len(msg)) + msg
	sock.sendall(msg)

def read_message(sock, decryptor_function):
	# Read message length and unpack it into an integer
	raw_msglen = recvall(sock, 4)
	if not raw_msglen:
		return None
	msglen = struct.unpack('>I', raw_msglen)[0]
	# Read the message data
	msg = recvall(sock, msglen)
	msg = decryptor_function(msg)
	msg = bson.loads(msg)
	return msg

def recvall(sock, n):
	# Helper function to recv n bytes or return None if EOF is hit
	data = b''
	while len(data) < n:
		packet = sock.recv(n - len(data))
		if not packet:
			return None
		data += packet
	return data
