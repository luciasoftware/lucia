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

import pygame
from .. import globals

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

def text_objects(text, font):
	textSurface = font.render(text, True, white)
	return textSurface, textSurface.get_rect()

def display_text(text):
	pygame.display.get_surface().fill(black)
	largeText = pygame.font.SysFont('arial',42)
	TextSurf, TextRect = text_objects(text, largeText)
	w, h = pygame.display.get_surface().get_size()
	TextRect.center = ((w/2.5),(h/2.5))
	pygame.display.get_surface().blit(TextSurf, TextRect)
	pygame.display.update()
