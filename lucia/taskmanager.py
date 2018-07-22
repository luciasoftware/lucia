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

import threading

class Task(threading.Thread):
	def __init__(self, func):
		self.func = func
		self.running = False

	def run(self):
		running = True
		self.result = self.func()

	def is_running(self):
		return self.running

	def get_result(self):
		return self.result

class TaskManager():
	def __init__(self):
		self.tasks = {}

	def create_task(self, name, func):
		t = Task(func)
		self.tasks[name] = t
		t.run()

	def get_task(self, name):
		return self.tasks[name]
