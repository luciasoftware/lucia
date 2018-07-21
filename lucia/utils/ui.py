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
