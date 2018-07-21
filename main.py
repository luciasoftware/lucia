import sys

def foo(exctype, value, tb):
	print("Error Information")
	print("Type:" + str(exctype))
	print("Value:" + str(value))
	print("Traceback:" + str(tb))
	with open("error.log", "a+") as myfile:
		myfile.write("Error information.\nType: " + str(exctype) + "\nValue: " + str(value) + "\nTraceback: " + str(tb) + "\n\n")

#sys.excepthook = foo

import pygame, lucia

from lucia import *
from lucia.interface import *
from lucia.utils import *
import time

version = "0.2"
version_url = "https://repo.accessiware.com/bgt/games/redspot/version.txt"
download_url = "https://gaming.accessiware.com"
s = SpeechSystem("test123")
ress = ResourceManager()
updater = Updater(version, version_url, download_url)
if updater.check_for_updates():
	updater.perform_update()
test = Sound()


def game_exit():
	lucia.quit()
	sys.exit()

def preload():
	s.first_time_configuration()
	s.get_male_voice().speak("Loading. Please wait!")
	ress.load_resources("resources.dat", "test123")
	test.load(ress.get("music.wav"))
	#test.set_volume(20)

def main():
	mainmenu = Menu()
	mainmenu.add_speech_method(s.get_screen_reader())
	mainmenu.add_item_tts("Start game", "start")
	mainmenu.add_item_tts("reconfigure Voices", "voiceconfig")
	mainmenu.add_item_tts("Exit game", "exit")
	result = mainmenu.run("Main menu. Select shit now!")
	if result == "start":
		play()
		main()
	if result == "voiceconfig":
		s.setup()
		main()
	if result == "-1" or result == "exit":
		s.get_screen_reader().speak("Thanks for playing", True)
		game_exit()

def play():
	clock = pygame.time.Clock()
	player = vector()
	direction = 90
	pool = SoundPool()
	pool.update_listener_3d(0,0,0)
	pool.play_3d(ress.get("test.wav"), 10, 10, 0, True)

	while True:
		clock.tick(30)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit()
			elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
				return
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					s.get_screen_reader().speak(str(round(player.x,2)) + " " + str(round(player.y,2)) + " " + str(round(player.z,2)))
				if event.key == pygame.K_f:
					s.get_screen_reader().speak(str(direction))
				if event.key == pygame.K_q:
					direction = turnleft(direction)
				if event.key == pygame.K_e:
					direction = turnright(direction)
				if event.key == pygame.K_w:
					player = move((player.x,player.y,player.z), direction)
				if event.key == pygame.K_d:
					player = move((player.x,player.y,player.z), direction-90)
				if event.key == pygame.K_s:
					player = move((player.x,player.y,player.z), direction+180)
				if event.key == pygame.K_a:
					player = move((player.x,player.y,player.z), direction+90)
		pool.update_listener_3d(player.x,player.y,player.z, direction)
		pygame.event.pump()

if __name__ == "__main__":
	lucia.init("LuciaSoftware", "TheRepoGame")
	preload()
	main()
