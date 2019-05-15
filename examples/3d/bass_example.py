import sys
sys.path.append(".")

import time
import lucia

lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()
player = lucia.utils.rotation.Vector()
direction = 90


while True:
	lucia.process_events()
	if lucia.key_pressed(lucia.SDLK_w):
		player = lucia.utils.rotation.move(player.getcoords(), direction)
	if lucia.key_pressed(lucia.SDLK_a):
		player = lucia.utils.rotation.move(player.getcoords(), direction-90)
	if lucia.key_pressed(lucia.SDLK_s):
		player = lucia.utils.rotation.move(player.getcoords(), direction+180)
	if lucia.key_pressed(lucia.SDLK_d):
		player = lucia.utils.rotation.move(player.getcoords(), direction+90)
	if lucia.key_pressed(lucia.SDLK_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(lucia.SDLK_c):
		lucia.output.output(f"Cors {player.x}, {player.y}, {player.z}")
	time.sleep(.005)

