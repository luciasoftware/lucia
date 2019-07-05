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
	msg = struct.pack(">I", len(msg)) + msg
	sock.sendall(msg)


def read_message(sock, decryptor_function):
	# Read message length and unpack it into an integer
	raw_msglen = recvall(sock, 4)
	if not raw_msglen:
		return None
	msglen = struct.unpack(">I", raw_msglen)[0]
	# Read the message data
	msg = recvall(sock, msglen)
	msg = decryptor_function(msg)
	msg = bson.loads(msg)
	return msg


def recvall(sock, n):
	# Helper function to recv n bytes or return None if EOF is hit
	data = b""
	while len(data) < n:
		packet = sock.recv(n - len(data))
		if not packet:
			return None
		data += packet
	return data
