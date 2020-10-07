import lucia
lucia.initialize()
lucia.show_window('test')
d=lucia.ui.dialogs.message_dialog('hello world!')
while 1:
	d.run()