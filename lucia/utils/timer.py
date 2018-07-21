import time

class Timer():
	def __init__(self):
		self.inittime=int(round(time.time() * 1000))

	def elapsed(self):
		return int(round(time.time() * 1000))-self.inittime

	def restart(self):
		self.inittime=int(round(time.time() * 1000))