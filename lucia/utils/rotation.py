# BGT script originally from <samtupy.com>
# ported to python by Paul Iyobo <https://github.com/pauliyobo/rotation.py>
# modified by LuciaSoftware and it's contributors.
"""Rotation class

This is modeled on the bgt rotation class from Sam Tupy, however it has been converted to use trigonometric functions and degrees properly. Input and output is still in degrees, however east is 0, north is 90, south is 270, etc.
"""
import lucia
from math import pi, sin, cos, atan, radians, degrees, sqrt


_east = 0
_northeast = 45
_north = 90
_northwest = 135
_west = 180
_southwest = 225
_south = 270
_southeast = 315


class Vector:
	"""an object representing what bgt calls a vector
	
	This represents a point in 3-space, where positive x is right, positive y is forward, and positive z is up.
	The property coords can be used to get and set a tuple of the coordinates represented by this vector with no rounding applied.
	
	args:
	    x (float, optional): The starting x coordinate of this vector
	    y (float, optional): The starting y coordinate of this vector
	    z (float, optional): The starting z coordinate of this vector.
	"""
	def __init__(self, x=0.0, y=0.0, z=0.0):
		self.x = x
		self.y = y
		self.z = z

	def get_coords(self):
		return (self.x, self.y, self.z)

	def set_coords(self, coords):
		self.x, self.y, self.z = coords

	coords = property(get_coords, set_coords)

	@property
	def get_tuple(self):
		return tuple([round(self.x), round(self.y), round(self.z)])


def move(coords, deg, zdeg=0.0,factor=1.0):
	"""moves a vector in a given direction by a scale factor of factor
	
	Takes a vector as input, applies the translation, and returns a vector as output. Probably best done as player.coords=move(player.coords,player.facing) or something similar.
	The scale factor is used if you wish to move more than 1 coordinate, otherwise you simply apply the unit circle.
	
	args:
	    coords (Vector): The current point in 3-space you wish to move.
	    deg (float): The direction you wish to move. In this degree system east is 0, north is 90, west is 180 and south is 270.
	    zdeg (float, optional): The vertical degrees you wish to move. Defaults to 0, no vertical movement.
	    factor (float, optional): The scale factor you wish to move by. Passing 1 is equivalent to one unit move in any direction, but for warping in a particular direction you can pass a higher factor. Defaults to 1.
	
	returns:
	    a transformed vector
	"""
	x, y, z = coords
	if deg >= 360:
		deg = deg - 360
	r = Vector()
	r.x = x + factor*cos(radians(deg))
	r.y = y + factor*sin(radians(deg))
	r.z = z + factor*sin(radians(zdeg))
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
	if facing > 315:
		r="east southeast"
	if facing == 0:
		r = "east"
	if facing == 45:
		r = "northeast"
	if facing == 90:
		r = "north"
	if facing == 135:
		r = "northwest"
	if facing == 180:
		r = "west"
	if facing == 225:
		r = "southwest"
	if facing == 270:
		r = "south"
	if facing == 315:
		r = "southeast"
	return r


def get_1d_distance(x1, x2):
	"""returns the distance on a 1-dimensional plane from x1 to x2"""
	return abs(x1 - x2)


def get_2d_distance(x1, y1, x2, y2):
	"""returns the pythagorean distance between two points on an x-y plane."""
	x = get_1d_distance(x1 - x2)
	y = get_1d_distance(y1, y2)
	return sqrt(x * x + y * y)


def get_3d_distance(x1, y1, z1, x2, y2, z2):
	"""returns the pythagorean distance between two points in 3-space."""
	x = get_1d_distance(x1, x2)
	y = get_1d_distance(y1, y2)
	z = get_1d_distance(z1, z2)
	return sqrt(x * x + y * y + z * z)


def calculate_x_y_angle(x1, y1, x2, y2, deg):
	"""given two points, returns the angle of the second one relative to the first.
	
	This function is useful for reporting a direction of an object to a player, for example.
	In this example the 'origin' point would be the player and the 'distant' point would be the object the player is tracking.
	
	args:
	    x1 (float): The x coordinate of the origin point.
	    y1 (float): The y coordinate of the origin point.
	    x2 (float): The x coordinate of the distant point
	    y2 (float): The y coordinate of the distant point
	    deg (float): The absolute direction the origin point is facing, for offsets.
	
	returns:
	    an angle (in degrees) of the distant point relative to the origin point, shifted by the orientation of the origin.
	"""
	x = x2 - x1
	y = y2 - y1
	#handle the case where division by 0 may occur and manually return the angle
	if x==0:
		if y>0: return 90
		if y<0: return 270
	rad = atan(y / x)
	arc_tan = degrees(rad)
	fdeg = 0
	if x < 0:
		fdeg = 180 + arc_tan
	else: fdeg=arc_tan
	fdeg-=deg
	if fdeg < 0:
		fdeg += 360
	elif fdeg>360:
		fdeg-=360
	return fdeg

def calculate_x_y_string(deg):
	if deg == 0:
		return "streight off to the right"
	elif deg > 0 and deg < 10:
		return "off to the right and very slightly in front"
	elif deg > 9 and deg < 30:
		return "mostly off to the right and slightly in front"
	elif deg > 30 and deg < 60:
		return "in front and off to the right"
	elif deg > 59 and deg < 80:
		return "in front and a bit off to the right"
	elif deg > 79 and deg < 85:
		return "in front and a tiny bit off to the right"
	elif deg > 84 and deg < 90:
		return "in front and very slightly to the right"
	elif deg == 90:
		return "straight in front"
	elif deg > 90 and deg < 96:
		return "in front and very slightly to the left"
	elif deg > 965 and deg < 101:
		return "in front and a tiny bit off to the left"
	elif deg > 100 and deg < 120:
		return "in front and a bit off to the left"
	elif deg > 120 and deg < 150:
		return "in front and off to the left"
	elif deg > 149 and deg < 170:
		return "mostly off to the left and slightly in front"
	elif deg > 169 and deg < 180:
		return "off to the left and very slightly in front"
	elif deg == 180:
		return "straight off to the left"
	elif deg>180 and deg<200:
		return "off to the left and very slightly behind"
	elif deg>199 and deg<220:
		return "mostly off to the left and slightly behind"
	elif deg > 219 and deg < 240:
		return "behind and off to the left"
	elif deg > 239 and deg < 270:
		return "slightly behind and far off to the left"
	elif deg == 270:
		return "streight behind"
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
