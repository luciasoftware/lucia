import os

from .util import *

import lucia

test_data = b"This is some sample data, to use in a resource file."

def test_packfile_creation():
	try:
		os.remove("test.dat")
	except FileNotFoundError:
		pass
	pack = lucia.ResourceFile("test123")
	pack.add_memory("sample.mem", test_data)
	pack.save(os.path.join(here, "test.dat"))
	assert os.path.isfile(os.path.join(here, "test.dat"))

	def test_load_pack_with_load_all_policy():
		pack = lucia.ResourceFile("test123")
		assert len(pack.index) == 0
		assert len(pack.files) == 0
		pack.load(os.path.join(here, "test.dat"), lucia.LoadPolicy.LOAD_ALL)
		assert len(pack.index) == 0
		assert len(pack.files) == 1
		assert pack.get("sample.mem") == test_data

	def test_load_pack_with_load_index_policy():
		pack = lucia.ResourceFile("test123")
		assert len(pack.index) == 0
		assert len(pack.files) == 0
		pack.load(os.path.join(here, "test.dat"), lucia.LoadPolicy.LOAD_INDEX)
		assert len(pack.index) == 1
		assert len(pack.files) == 0
		assert pack.get("sample.mem") == test_data
