# BGT script originally from <samtupy.com>
# ported to python by Paul Iyobo <https://github.com/pauliyobo/rotation.py>
# modified by LuciaSoftware and it's contributors.

import lucia
from math import pi, sin, cos, atan, radians, sqrt


_east = 0
_northeast = 45
_north = 90
_northwest = 135
_west = 180
_southwest = 225
_south = 270
_southeast = 315


class Vector:
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = x
		self.y = y
		self.z = z

	def get_coords(self):
		return (self.x, self.y, self.z)

	def set_coords(self, cords):
		self.x, self.y, self.z = coords

	coords = property(get_coords, set_coords)

	@property
	def get_tuple(self):
		return tuple([round(self.x), round(self.y), round(self.z)])


def move(coords, deg=0.0, zdeg=0.0):
	x, y, z = coords
	if deg >= 360:
		deg = deg - 360
	r = Vector()
	# If using bass, we are using bgt's style of handling coors for now, x is left and right, y is forward and backwards and z is up and down.
	if isinstance(lucia.audio_backend_class, lucia.audio.bass.BassAudioBackend):
		r.x = x + sin(radians(deg))
		r.y = y + cos(radians(deg))
		r.z = z + sin(radians(zdeg))
		return r
	else:  # if using openal or fmod
		r.x = x + cos(radians(deg))
		r.y = y + sin(radians(deg))
		r.z = z + sin(radians(zdeg))
		return r


def getdir(facing):
	if facing <= _north and facing > _northeast:
		return _north
	if facing <= _northeast and facing > _east:
		return _northeast
	if facing == 0 or facing > 315:
		return _east
	if facing <= _southeast and facing > _south:
		return _southeast
	if facing <= _south and facing > _southwest:
		return _south
	if facing <= _southwest and facing > _west:
		return _southwest
	if facing <= _west and facing > _northwest:
		return _west
	if facing <= _northwest and facing > _north:
		return _northwest
	return -1


def snapleft(direction, inc=45):
	d = direction + inc
	if d >= 360:
		d -= 360
	return d


def snapright(direction, inc=45):
	d = direction - inc
	if d < 0:
		d += 360
	return d


def turnleft(deg, inc=5):
	deg += inc
	if deg >= 360:
		deg -= 360
	return deg


def turnright(deg, inc=5):
	deg -= inc
	if deg < 0:
		deg += 360
	return deg


def dir_to_string(facing):
	r = str()
	if facing > 0 and facing < 45:
		r = "east north east"
	if facing > 315:
		r = "east south east"
	if facing > 45 and facing < 90:
		r = "north north east"
	if facing > 90 and facing < 135:
		r = "north north west"
	if facing > 135 and facing < 180:
		r = "west north west"
	if facing > 180 and facing < 225:
		r = "west south west"
	if facing > 225 and facing < 270:
		r = "south south west"
	if facing > 270 and facing < 315:
		r = "south south east"
	if facing == 0:
		r = "east"
	if facing == 45:
		r = "north east"
	if facing == 90:
		r = "north"
	if facing == 135:
		r = "north west"
	if facing == 180:
		r = "west"
	if facing == 225:
		r = "south west"
	if facing == 270:
		r = "south"
	if facing == 315:
		r = "south east"
	return r


def get_1d_distance(x1, x2):
	return abs(x1 - x2)


def get_2d_distance(x1, y1, x2, y2):
	x = get_1d_distance(x1 - x2)
	y = get_1d_distance(y1, y2)
	return sqrt(x * x + y * y)


def get_3d_distance(x1, y1, z1, x2, y2, z2):
	x = get_1d_distance(x1, x2)
	y = get_1d_distance(y1, y2)
	z = get_1d_distance(z1, z2)
	return sqrt(x * x + y * y + z * z)


def calculate_x_y_angle(x1, y1, x2, y2):
	x = x2 - x1
	y = y2 - y1
	if x == 0:
		x += 0.0000001
	if y == 0:
		y += 0.0000001
	rad = atan(y / x)
	arc_tan = rad / pi * 180
	fdeg = 0
	if x > 0:
		fdeg = 90 - arc_tan
	elif x < 0:
		fdeg = 270 - arc_tan
	if x == 0:
		if y > 0:
			fdeg = 0
		elif y < 0:
			fdeg = 180
	fdeg = 0
	fdeg -= deg
	if fdeg < 0:
		fdeg += 360
	fdeg = round(fdeg, 1)
	return fdeg


def calculate_x_y_angle(x1, y1, x2, y2):
	x = x2 - x1
	y = y2 - y1
	if x == 0:
		x += 0.0000001
	if y == 0:
		y += 0.0000001
	rad = atan(y / x)
	arc_tan = rad / pi * 180
	fdeg = 0
	if x > 0:
		fdeg = 90 - arc_tan
	elif x < 0:
		fdeg = 270 - arc_tan
	if x == 0:
		if y > 0:
			fdeg = 0
		elif y < 0:
			fdeg = 180
	fdeg = 0
	fdeg -= deg
	if fdeg < 0:
		fdeg += 360
	fdeg = round(fdeg, 1)
	return fdeg


def calculate_x_y_string(deg):
	if deg == 0:
		return "streight off to the right"
	elif deg > 0 and deg < 10:
		return "mostly off to the right and a little bit in front"
	elif deg > 9 and deg < 30:
		return "mostly off to the right and slightly in front"
	elif deg > 30 and deg < 60:
		return "in front and off to the right"
	elif deg > 59 and deg < 80:
		return "in front and slightly off to the right"
	elif deg > 79 and deg < 85:
		return "in front and very slightly off to the right"
	elif deg > 84 and deg < 90:
		return "straight in front and a little bit off to the right"
	elif deg == 90:
		return "straight in front"
	elif deg > 90 and deg < 96:
		return "straight in front and a little bit off to the left"
	elif deg > 96 and deg < 101:
		return "in front and very slightly off to the left"
	elif deg > 100 and deg < 120:
		return "in front and slightly off to the left"
	elif deg > 120 and deg < 150:
		return "in front and off to the left"
	elif deg > 149 and deg < 170:
		return "mostly off to the left and slightly in front"
	elif deg > 169 and deg < 180:
		return "mostly off to the left and a little bit in front"
	elif deg == 180:
		return "straight off to the left"

	elif deg > 219 and deg < 240:
		return "behind and a fair distance off to the left"
	elif deg > 239 and deg < 270:
		return "slightly behind and far off to the left"
	elif deg == 270:
		return "streight off to the left"
	elif deg > 270 and deg < 300:
		return "far off to the left"
	elif deg > 299 and deg < 320:
		return "a ways off to the left"
	elif deg > 319 and deg < 340:
		return "a little ways off to the left"
	elif deg > 339 and deg < 350:
		return "slightly off to the left"
	elif deg > 349 and deg < 360:
		return "verry slightly off to the left"
	return ""
