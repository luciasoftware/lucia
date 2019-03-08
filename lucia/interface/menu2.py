"""enhanced menu for advance uses. Make sure you create wx.App and call the menu before creating any menus with this module. See examples/demmo1/main2.py if you need an idea how this module is used"""
import wx
import lucia
from lucia.audio.soundpool import *
import logging
logging.basicConfig(filename="menu tracebacks.log", level=logging.DEBUG)

#Events
CANCELEVENT=0

import sys
import time
from lucia import output
class SpinboxDialog(wx.Dialog):
    def __init__(self, parent, title, caption, value=0):
        style = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
        super(SpinboxDialog, self).__init__(parent, -1, title, style=style)
        text = wx.StaticText(self, -1, caption)
        input = wx.SpinCtrl(self, -1, value=str(value), max=2000000000, size=(400,300))
        buttons = self.CreateButtonSizer(wx.OK|wx.CANCEL)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(text, 0, wx.ALL, 5)
        sizer.Add(buttons, 0, wx.EXPAND|wx.ALL, 5)
        sizer.Add(input, 1, wx.EXPAND|wx.ALL, 5)
        input.SetFocus()
        self.SetSizerAndFit(sizer)
        self.input = input
    def SetValue(self, value):
        self.input.SetValue(value)
    def GetValue(self):
        return self.input.GetValue()

def getinput(title, message, multiline=False, value="", mode="plaintext"):
	text=""
	if mode=="plaintext":
		if multiline:
			input=TextEntryDialog(None, message, title)
		else:
			input=wx.TextEntryDialog(None, message, title)
		input.SetValue(value)
		input.ShowModal()
		text=input.GetValue()
		input.Destroy()
	elif mode=="spinbox":
		input=SpinboxDialog(None, message, title)
		input.SetValue(value)
		input.ShowModal()
		text=input.GetValue()
		input.Destroy()
	return text

class menuitem:
	def __init__(self, name, can_return=False, has_value=False, value="", value_mode="plaintext", can_be_toggled=False, toggle_value=False, can_activate=True, on_focus=None, event=None):
		self.name=name
		self.has_value=has_value
		self.value_mode=value_mode
		self.value=value
		self.can_be_toggled=can_be_toggled
		self.toggle_value=toggle_value
		self.can_return=can_return
		self.can_activate=can_activate
		self.on_focus=on_focus #Make sure this is a function. This event is called whenever the focus is on this menu item
		self.event=event #This is usually an integer. See the events section of this file. Set this to any of the events in the events section.
class Menu:
	def __init__(self, items, clicksound="", edgesound="", wrapsound="", entersound="", opensound="", itempos=0, title="menu", fpscap=120, on_index_change=None):
		self.clicksound=clicksound
		self.edgesound=edgesound
		self.wrapsound=wrapsound
		self.entersound=entersound
		self.opensound=opensound
		self.itempos=itempos
		self.items=items
		self.title=title
		self.fpscap=fpscap
		self.on_index_change=on_index_change #make sure this is a function. It is called whenever the index of a menu is changed. The index change happens whenever user cycles between menu items.
		self.pool=SoundPool()
	
	def run(self):
		try:
			output.speak(self.title)
			return self.loop()
		except Exception as e:
			output.speak(str(e))
	def loop(self):
		while 1:
			time.sleep(0.005)
			try:
				lucia.process_events()
				if lucia.key_pressed(lucia.SDLK_RETURN):
					if self.items[self.itempos].can_return:
						if self.entersound != "": source=self.pool.play_stationary(self.entersound)
						list_values=[]
						if self.items[self.itempos].event==CANCELEVENT:
							return list_values
						for x in self.items:
							if x.name != self.items[self.itempos].name:
								list_values.append({"name": x.name, "value": x.value, "toggle_value": x.toggle_value})
						list_values.insert(0, {"name": self.items[self.itempos].name, "value": self.items[self.itempos].value, "toggle_value": self.items[self.itempos].toggle_value})
						return list_values
				elif lucia.key_pressed(lucia.SDLK_UP):
					if self.itempos > 0:
						self.itempos-=1
						if self.clicksound != "": clicksound=self.pool.play_stationary(self.clicksound)
						if self.items[self.itempos].on_focus!=None:
							self.items[self.itempos].on_focus()
						if self.on_index_change!=None:
							self.on_index_change()
						if self.items[self.itempos].has_value==False and self.items[self.itempos].can_be_toggled==False:
							output.speak(self.items[self.itempos].name)
						elif self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled==False:
							output.speak(self.items[self.itempos].name+": "+str(self.items[self.itempos].value)+". Press left shift or right shift to change this item's value")
						elif self.items[self.itempos].has_value==False and self.items[self.itempos].can_be_toggled:
							if self.items[self.itempos].toggle_value==True:
								output.speak(self.items[self.itempos].name+": On. Press space to switch off")
							else:
								output.speak(self.items[self.itempos].name+": Off. Press space to switch on")
						elif self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled:
							speakstr=self.items[self.itempos].name+". Value: "+str(self.items[self.itempos].value)
							if self.items[self.itempos].toggle_value==True:
								speakstr+=". Switch: On"
							else:
								speakstr+=". Switch: Off"
							output.speak(speakstr+". Press left shift or right shift to change this item's value. Press space to toggle on or off")
				elif lucia.key_pressed(lucia.SDLK_DOWN):
					if self.itempos < len(self.items)-1:
						self.itempos+=1
						if self.clicksound != "": clicksound=self.pool.play_stationary(self.clicksound)
						if self.items[self.itempos].on_focus!=None:
							self.items[self.itempos].on_focus()
						if self.on_index_change!=None:
							self.on_index_change()
						if self.items[self.itempos].has_value==False and self.items[self.itempos].can_be_toggled==False:
							output.speak(self.items[self.itempos].name)
						elif self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled==False:
							output.speak(self.items[self.itempos].name+": "+str(self.items[self.itempos].value)+". Press left shift or right shift to change this item's value")
						elif self.items[self.itempos].has_value==False and self.items[self.itempos].can_be_toggled:
							if self.items[self.itempos].toggle_value==True:
								output.speak(self.items[self.itempos].name+": On. Press space to switch off")
							else:
								output.speak(self.items[self.itempos].name+": Off. Press space to switch on")
						elif self.items[self.itempos].has_value and self.items[self.itempos].can_be_toggled:
							speakstr=self.items[self.itempos].name+". Value: "+str(self.items[self.itempos].value)
							if self.items[self.itempos].toggle_value==True:
								speakstr+=". Switch: On"
							else:
								speakstr+=". Switch: Off"
							output.speak(speakstr+". Press left shift or right shift to change this item's value. Press space to toggle on or off")
				elif lucia.key_pressed(lucia.SDLK_SPACE):
					if self.itempos>-1 and self.itempos<len(self.items):
						if self.items[self.itempos].can_be_toggled:
							if self.entersound != "": entersound=self.pool.play_stationary(self.entersound)
							if self.items[self.itempos].toggle_value==True:
								output.speak("off")
								self.items[self.itempos].toggle_value=False
							else:
								output.speak("on")
								self.items[self.itempos].toggle_value=True
				elif lucia.key_pressed(lucia.SDLK_LSHIFT) or lucia.key_pressed(lucia.SDLK_RSHIFT):
					if self.items[self.itempos].has_value==True:
						self.items[self.itempos].value=getinput("change value", self.items[self.itempos].name+". ", value=self.items[self.itempos].value, mode=self.items[self.itempos].value_mode)
						output.speak("value set to "+str(self.items[self.itempos].value))
						if self.entersound != "": entersound=self.pool.play_stationary(self.entersound)
			except Exception as e:
				output.speak(str(e))
