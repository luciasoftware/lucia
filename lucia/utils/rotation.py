# BGT script originally from <samtupy.com>
# ported to python by Paul Iyobo <https://github.com/pauliyobo/rotation.py>
# modified by LuciaSoftware and it's contributors.
"""Rotation class

This is modeled on the bgt rotation class from Sam Tupy. Input and output are in degrees.
"""
import lucia
from math import pi, sin, cos, atan2, radians, degrees, sqrt

# Directions.
_east = 90
_northeast = 45
_north = 0
_northwest = 315
_west = 270
_southwest = 225
_south = 180
_southeast = 135
#Should only be used for moving upwards on the z axes, has not been tested with right handed coordinate system yet
_straight_up = 90
_straight_down = -90

# Coordinate systems

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

def move(coords, deg, pitch=0.0,factor=1.0):
	"""moves a vector in a given direction by a scale factor of factor
	
	Takes a vector as input, applies the translation, and returns a vector as output. Probably best done as player.coords=move(player.coords,player.facing) or something similar.
	The scale factor is used if you wish to move more than 1 coordinate, otherwise you simply apply the unit circle.
	
	args:
			coords (tuple or list): The current point in 3-space you wish to move.
			deg (float): The current facing of an object
			pitch (float, optional): The vertical degrees you wish to move. Defaults to 0, no vertical movement.
			factor (float, optional): The scale factor you wish to move by. Passing 1 is equivalent to one unit move in any direction, but for warping in a particular direction you can pass a higher factor. Defaults to 1.
	
	returns:
			a transformed vector
	"""
	x, y, z = coords
	steplength=factor*cos(radians(pitch))
	r = Vector()
	r.x = x + steplength*sin(radians(deg))
	r.y = y + steplength*cos(radians(deg))
	r.z = z + factor*sin(radians(pitch))
	return r
def calculate_angle(x1, y1, x2, y2, deg):
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
		if y >= 0: return 0
		if y < 0: return 180
	rad = atan2(y, x)
	arc_tan = degrees(rad)
	fdeg = 0
	if x < 0:
		fdeg = 270 - arc_tan
	elif x > 0:
		fdeg = 270 - arc_tan
	fdeg-=deg
	if fdeg < 0:
		fdeg += 360
	elif fdeg>360:
		fdeg-=360
	return fdeg

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
	d = direction - inc
	if d >= 360:
		d -= 360
	return d


def snapright(direction, inc=45):
	d = direction + inc
	if d < 0:
		d += 360
	return d


def turnleft(deg, inc=5):
	deg -= inc
	if deg < 0:
		deg += 360
	return deg


def turnright(deg, inc=5):
	deg += inc
	if deg >= 360:
		deg -= 360
	return deg


def get_1d_distance(x1, x2):
	"""returns the distance on a 1-dimensional plane from x1 to x2"""
	return abs(x1 - x2)


def get_2d_distance(x1, y1, x2, y2):
	"""returns the pythagorean distance between two points on an x-y plane."""
	x = get_1d_distance(x1, x2)
	y = get_1d_distance(y1, y2)
	return sqrt(x * x + y * y)


def get_3d_distance(x1, y1, z1, x2, y2, z2):
	"""returns the pythagorean distance between two points in 3-space."""
	x = get_1d_distance(x1, x2)
	y = get_1d_distance(y1, y2)
	z = get_1d_distance(z1, z2)
	return sqrt(x * x + y * y + z * z)
