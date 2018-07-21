from math import pi, sin, cos, atan, radians, sqrt


_east = 0
_northeast = 45
_north = 90
_northwest = 135
_west = 180
_southwest = 225;
_south = 270
_southeast = 315


class vector:
 def __init__(self, x=0.0, y=0.0, z=0.0):
  self.x = x
  self.y= y
  self.z = z

 @property
 def getcoords(self):
  return (self.x, self.y, self.z)

 @property
 def get_tuple(self):
  return tuple([round(self.x),round(self.y),round(self.z)])

def move(coords, deg=0.0, zdeg=0.0):
	x, y, z = coords
	if deg > 360:
		deg = deg - 360
	r = vector()
	r.x=x+cos(radians(deg))
	r.y=y+sin(radians(deg))
	r.z=z+sin(radians(zdeg))
	return r

def getdir(facing):
 if facing>=_north and facing<_northeast:
  return _north
 if facing>=_northeast and facing<_east:
  return _northeast
 if facing>=_east and facing<_southeast:
  return _east
 if facing>=_southeast and facing<_south:
  return _southeast
 if facing >= _south and facing <_southwest:
  return _south
 if facing >= _southwest and facing < _west:
  return _southwest
 if facing >= _west and facing<_northwest:
  return _west
 return -1 

def snapleft(direction, inc=45):
 d = direction+inc
 if d>360:
  d-=360
 return d

def snapright(direction, inc=45):
 d = direction-inc
 if d<0:
  d+=360
 return d

def turnleft(deg, inc=5):
 deg+=inc
 if deg>360:
  deg-=360
 return deg

def turnright(deg, inc=5):
 deg-=inc
 if deg<0:
  deg+=360
 return deg

def dir_to_string(direction):
 r=str(int(direction))
 r=r.replace(str(_northwest), "northwest")
 r=r.replace(str(_west), "west")
 r=r.replace(str(_southwest), "southwest")
 r=r.replace(str(_south), "south")
 r=r.replace(str(_southeast), "southeast")
 r=r.replace(str(_east), "east")
 r=r.replace(str(_northeast), "northeast")
 r=r.replace(str(_north), "north")
 return r


def get_1d_distance(x1, x2):
 return abs(x1-x2)

def get_2d_distance(x1, y1, x2, y2):
 x=get_1d_distance(x1-x2)
 y= get_1d_distance(y1, y2)
 return sqrt(x*x+y*y)

def get_3d_distance(x1, y1, z1, x2, y2, z2):
 x=get_1d_distance(x1, x2)
 y=get_1d_distance(y1, y2)
 z=get_1d_distance(z1, z2)
 return sqrt(x*x+y*y+z*z)

def calculate_x_y_angle(x1, y1, x2, y2):
 x = x2-x1
 y=y2-y1
 if x == 0:
  x+=0.0000001
 if y == 0:
  y+=0.0000001
 rad = atan(y/x)
 arc_tan = rad/pi*180
 fdeg = 0
 if x>0:
  fdeg=90-arc_tan
 elif x<0:
  fdeg = 270-arc_tan
 if x == 0:
  if y>0:
   fdeg = 0
  elif y<0:
   fdeg=180
 fdeg=0
 fdeg-=deg
 if fdeg<0:
  fdeg+=360
 fdeg = round(fdeg, 1)
 return fdeg

def calculate_x_y_string(deg):
 if deg == 0 or deg == 360:
  return 'streight in front'
 elif deg>0 and deg<10:
  return 'Verry slightly to the Right'
 elif deg>9 and deg<20:
  return 'Slightly off to the right'
 elif deg>19 and deg<40:
  return 'A little ways off to the right'
 elif deg>39 and deg<90:
  return 'A fair distance off to the right'
 elif deg == 90:
  return 'streight off to the right'
 elif deg>90 and deg<120:
  return 'slightly behind and far off to the right'
 elif deg>119 and deg<150:
  return 'behind and a little ways off to the right'
 elif deg>149 and deg<170:
  return 'behind and slightly to the right'
 elif deg>169 and deg<180:
  return 'behind and verry slightly to the right'
 elif deg == 180:
  return 'streight behind'
 elif deg>180 and deg<190:
  return 'behind and verry slightly to the left'
 elif deg>189 and deg<200:
  return 'behind and slightly to the left'
 elif deg>199 and deg<220:
  return 'behind and a little ways off to the lef'
 elif deg>219 and deg<240:
  return 'behind and a fair distance off to the left'
 elif deg>239 and deg<270:
  return 'slightly behind and far off to the left'
 elif deg == 270:
  return 'streight off to the left'
 elif deg>270 and deg<300:
  return 'far off to the left'
 elif deg>299 and deg<320:
  return 'a ways off to the left'
 elif deg>319 and deg<340:
  return 'a little ways off to the left'
 elif deg>339 and deg<350:
  return "slightly off to the left"
 elif deg>349 and deg<360:
  return "verry slightly off to the left"
 return ''
