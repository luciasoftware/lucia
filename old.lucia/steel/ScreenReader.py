import accessible_output2.outputs.auto
from ..utils.ui import *

class ScreenReader():
	def __init__(self):
		self.o = accessible_output2.outputs.auto.Auto()

	def speak(self, text, interrupt=False):
		try:
			self.o.output(str(text), interrupt)
			displayText(str(text))
		except:
			import platform, wx
			if platform.system().lower() == "darwin":
				app = wx.App()
				err = wx.MessageDialog(None, "Error: Couldn't output through VoiceOver\nTo fix this, go to the VoiceOver Utility, and check the box \"Allow VoiceOver to be controlled by AppleScript.\"\nYou can find that checkbox on the \"General\" page of your VoiceOver utility.","VoiceOver Output Error", wx.OK)
				err.ShowModal()
				err.Destroy()
				speak(text)
