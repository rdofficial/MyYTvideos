#Importing the required modules
import pyautogui,time, os, sys
from pynput import keyboard

text = 'Happy Bombing'

def on_press(key):
	""" """

	if str(key) == 'Key.esc':
		sys.exit()
	elif str(key) == 'Key.enter':
		pyautogui.typewrite(text)
		pyautogui.press('enter')
		time.sleep(0.25)

try:
	with keyboard.Listener(on_press = on_press) as listener:
		listener.join()
except Exception as e:
	pass
finally:
	print('Exiting bomber')
