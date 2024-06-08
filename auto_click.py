import pyautogui
import time
import random
import pyscreeze
import os

def move_and_click():
	screen_width, screen_height = pyautogui.size()
	x, y = screen_width / 2, screen_height / 2
	delay = 3

	# positions = [
    #     (x, y - (screen_height / 20)),
    #     (x + (screen_width / 20), y - (screen_height / 18)),
    #     (x + (screen_width / 10), y - (screen_height / 12)),
    #     (x + (screen_width / 10), y - (screen_height / 10)),
    #     (x + (screen_width / 8), y - (screen_height / 9)),
    #     (x + (screen_width / 11), y - (screen_height / 20)),
    #     (x + (screen_width / 18), y - (screen_height / 18)),
    #     (x + (screen_width / 9), y - (screen_height / 16)),
    #     (x + (screen_width / 9), y - (screen_height / 14)),
    #     (x - (screen_width / 2.1), y - (screen_height / 6))
    # ]

	positions = [
        (x + (x / 4), y - (screen_height / 12)),
		(x + (x / 3), y + (screen_height / 24)),
		(x + (x / 10), y),
		(x - (x / 1.8), y - (screen_height / 5))
    ]

	for pos in positions:
		pyautogui.moveTo(pos[0], pos[1], duration=0.2)
		pyautogui.click()
		time.sleep(delay)

	time.sleep(1)

def shut_down():
	screen_width, screen_height = pyautogui.size()
	x, y = screen_width / 2, screen_height / 2

	pyautogui.moveTo((x * 2) - 30, (y * 0) + 30, duration=0.2)
	pyautogui.click()
	time.sleep(0.5)

	pyautogui.moveTo((x * 2) - 30, (y * 0) + (y / 3.2), duration=0.2)
	pyautogui.click()
	time.sleep(0.5)

	pyautogui.moveTo(x - (x / 10), y, duration=0.2)
	pyautogui.click()
	time.sleep(5)

	os.system("shutdown /s /t 1")

def eat_food():
	pyautogui.press('k')
	time.sleep(1)

def main():
	time.sleep(5)
	start_time = time.time()
	eat_time = start_time

	while True:
		current_time = time.time()

		if current_time - start_time > 36000:
			shut_down()
			break
		elif current_time - eat_time > 1800:
			eat_food()
			eat_time = current_time;
		else:
			move_and_click()

if __name__ == "__main__":
    main()