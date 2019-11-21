import lucia

lucia.initialize()
lucia.show_window()
test_input = lucia.ui.VirtualInput()
result = test_input.run()
print("You typed {}".format(result))
lucia.quit()
