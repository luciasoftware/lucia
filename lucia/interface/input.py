import pygame

def get_key():
	while True:
		event = pygame.event.poll()
		if event.type == pygame.KEYDOWN:
			return event.key
		else:
			pass

def simple_input(speech, intro, password=False):
	current_string = ""
	speech.speak(intro)
	while True:
		inkey = get_key()
		print(inkey)
		if inkey == pygame.K_BACKSPACE and current_string != "":
			if password:
				speech.speak("Star deleted", True)
			else:
				speech.speak(current_string[len(current_string)-1], + " deleted", True)
			current_string = current_string[0:-1]
		elif inkey == pygame.K_RETURN:
			break
		elif inkey == pygame.K_MINUS:
			current_string = current_string + "_"
		elif inkey <= 127:
			current_string= current_string + chr(inkey)
			if password:
				speech.speak("Star", True)
			else:
				speech.speak(chr(inkey), True)
	return current_string
