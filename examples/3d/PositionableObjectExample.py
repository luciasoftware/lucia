# note: This example needs an @audio.ogg@ file placed in the same directory to run.
import sys, os
sys.path.append(".")
import time
import lucia
import lucia.utils

lucia.initialize(audiobackend=lucia.AudioBackend.BASS)

#instantiate the player
player = lucia.utils.PositionableObject()

window = lucia.show_window()

pool = lucia.audio_backend.SoundPool()

s = pool.play_3d(
	os.path.join(os.getcwd(), "audio.ogg"), 0, 0, 0, 0, 0, 0, looping=True
)

while True:
	lucia.process_events()
	if lucia.key_pressed(lucia.K_LEFT):
		player.rotate_y(10)
	if lucia.key_pressed(lucia.K_RIGHT):
		player.rotate_y(-10)
	if lucia.key_pressed(lucia.K_w):
		player.position += player.forward
	if lucia.key_pressed(lucia.K_a):
		player.position += player.left
	if lucia.key_pressed(lucia.K_s):
		player.position += player.backward
	if lucia.key_pressed(lucia.K_d):
		player.position += player.right
	if lucia.key_pressed(lucia.K_q):
		lucia.quit()
		exit()
	if lucia.key_pressed(lucia.K_c):
		lucia.output.output(
			f"Cors {round(player.position.x,0)}, {round(player.position.y,0)}, {round(player.position.z,0)}"
		)
	if lucia.key_pressed(lucia.K_x):
		lucia.output.output(f"facing {player.direction_angle}")
# updating the listener position requires parameters in this order for compatibility with lucia current sistem, where z represents the vertical axis
	pool.update_listener_3d(player.position.x, player.position.z, player.position.y, player.direction_angle)
	time.sleep(0.005)