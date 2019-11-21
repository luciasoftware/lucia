# note> This example needs an @audio.ogg@ file placed in the same directory to run.
import sys, os

sys.path.append(".")

from math import radians
import time
import lucia
import lucia.utils
import pygame

lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()
player = lucia.utils.rotation.Vector()
direction = 0

s = pool.play_3d(
	os.path.join(os.getcwd(), "audio.ogg"), 5, 5, 0, 10, 10, 0, looping=True
)

while True:
	lucia.process_events()
	if lucia.key_pressed(pygame.K_LEFT):
		direction = lucia.utils.rotation.turnleft(direction, 10)
	if lucia.key_pressed(pygame.K_RIGHT):
		direction = lucia.utils.rotation.turnright(direction, 10)
	if lucia.key_pressed(pygame.K_w):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction)
	if lucia.key_pressed(pygame.K_a):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction - 90)
	if lucia.key_pressed(pygame.K_s):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction + 180)
	if lucia.key_pressed(pygame.K_d):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction + 90)

	if lucia.key_pressed(pygame.K_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(pygame.K_c):
		lucia.output.output(
			f"Cors {round(player.x,0)}, {round(player.y,0)}, {round(player.z,0)}"
		)
	if lucia.key_pressed(pygame.K_x):
		lucia.output.output(f"facing {direction}")
	pool.update_listener_3d(player.x, player.y, player.z, direction)
	time.sleep(0.005)