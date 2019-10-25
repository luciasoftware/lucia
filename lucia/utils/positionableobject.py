# Originally written by Alan Escola

import sys, os
import lucia
import pygame

class PositionableObject:
	'''represents a positionable object'''
	def rotate_y(self, degrees = 5):
		#applies the rotation translating lucia degrees sistem into the audio engine degrees sistem
		self.direction = self.direction.rotate_y(-degrees)
		#updates self._angle so north = 0, south = 180, etc
		degrees += self._angle
		if degrees >= 360:
			degrees -= 360
		elif degrees < 0:
			degrees += 360
		self._angle = degrees
		return self.direction_angle
	#variables
	_position = pygame.math.Vector3()
	_angle = 0
	direction = pygame.math.Vector3(0, 0, -1) # standard forward vector
	#properties to determine the relative directions
	@property
	def forward(self):
		return self.direction.rotate_y(180)
	@property
	def backward(self):
		return self.direction
	@property
	def right(self):
		return self.direction.rotate_y(-90)
	@property
	def left(self):
		return self.direction.rotate_y(90)
	#Translates the internal _angle to make it compatible with lucia
	@property
	def direction_angle(self):
		return 360 - self._angle
