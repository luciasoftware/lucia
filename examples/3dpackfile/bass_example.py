import sys, os

sys.path.append(".")

import time
import lucia
import lucia.utils

lucia.initialize()
r=lucia.ResourceFile("test")
r.load("sound/sound.pak")
lucia.set_global_resource_file(r)
window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()
player = lucia.utils.rotation.Vector()
direction = 0

s = pool.play_3d(
	"youtube2.ogg", 5, 5, 0, 10, 10, 0, looping=True
)

while True:
	lucia.process_events()
	if lucia.key_pressed(lucia.K_LEFT):
		direction = direction - 10
	if lucia.key_pressed(lucia.K_RIGHT):
		direction = direction + 10
	if lucia.key_pressed(lucia.K_w):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction)
	if lucia.key_pressed(lucia.K_a):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction - 90)
	if lucia.key_pressed(lucia.K_s):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction + 180)
	if lucia.key_pressed(lucia.K_d):
		player = lucia.utils.rotation.move((player.x, player.y, player.z), direction + 90)
	if lucia.key_pressed(lucia.K_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(lucia.K_c):
		lucia.output.output(
			f"Cors {round(player.x,0)}, {round(player.y,0)}, {round(player.z,0)}"
		)
	if lucia.key_pressed(lucia.K_x):
		lucia.output.output(f"facing {direction}")
	time.sleep(0.005)
	pool.update_listener_3d(
		round(player.x, 0), round(player.y, 0), round(player.z, 0), direction
	)
