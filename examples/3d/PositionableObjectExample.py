# note: This example needs an @audio.ogg@ file placed in the same directory to run.
import sys, os

sys.path.append(".")

import time
import lucia
import lucia.utils
import pygame

#instantiate the player
player = lucia.utils.PositionableObject()

lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()

s = pool.play_3d(
	os.path.join(os.getcwd(), "audio.ogg"), 0, 0, 0, 0, 0, 0, looping=True
)

while True:
	lucia.process_events()
	if lucia.key_pressed(pygame.K_LEFT):
		player.rotate_y(10)
	if lucia.key_pressed(pygame.K_RIGHT):
		player.rotate_y(-10)
	if lucia.key_pressed(pygame.K_w):
		player._position += player.forward
	if lucia.key_pressed(pygame.K_a):
		player._position += player.left
	if lucia.key_pressed(pygame.K_s):
		player._position += player.backward
	if lucia.key_pressed(pygame.K_d):
		player._position += player.right
	if lucia.key_pressed(pygame.K_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(pygame.K_c):
		lucia.output.output(
			f"Cors {round(player.position.x,0)}, {round(player.position.y,0)}, {round(player.position.z,0)}"
		)
	if lucia.key_pressed(pygame.K_x):
		lucia.output.output(f"facing {player.direction_angle}")
	pool.update_listener_3d(player._position.x, player._position.z, player._position.y, player.direction_angle)
	time.sleep(0.005)