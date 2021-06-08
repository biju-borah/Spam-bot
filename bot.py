from pynput.keyboard import Key, Controller
import time
Keyboard = Controller()
time.sleep(10)
for i in range(100):
    for letter in "This is bot":
        Keyboard.press(letter)
        Keyboard.release(letter)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)



