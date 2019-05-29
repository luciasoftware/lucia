import sys, os
sys.path.append(".")

import time
import lucia
import pygame

lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()
player = lucia.utils.rotation.Vector()
direction = 90

pool.play_3d(os.path.join(os.getcwd(), "examples", "3d", "youtube.wav"), 5, 5, 5).set_volume(.4)

while True:
	lucia.process_events()
	if lucia.key_down(pygame.K_w):
		player = lucia.utils.rotation.move((player.x,player.y,player.z), direction)
	if lucia.key_pressed(pygame.K_a):
		player = lucia.utils.rotation.move((player.x,player.y,player.z), direction-90)
	if lucia.key_pressed(pygame.K_s):
		player = lucia.utils.rotation.move((player.x,player.y,player.z), direction+180)
	if lucia.key_pressed(pygame.K_d):
		player = lucia.utils.rotation.move((player.x,player.y,player.z), direction+90)
	if lucia.key_pressed(pygame.K_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(pygame.K_c):
		lucia.output.output(f"Cors {round(player.x,0)}, {round(player.y,0)}, {round(player.z,0)}")
	time.sleep(.005)

