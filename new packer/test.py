from pack import *

p = ResourceFile("thisisatest", "0000000000000000", "thisisalongerheader")
p.add_file("hello.txt")
p.save("data.dat")

p2 = ResourceFile("thisisatest", "0000000000000000", "thisisalongerheader")
p2.load("data.dat")

f = open("hello.txt", "rb")
test_data = f.read()
f.close()

assert test_data == p2.get("hello.txt")