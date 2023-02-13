from digitalio import DigitalInOut, Direction, Pull
import board
import time


pin = DigitalInOut(board.GP7)
pin.direction = Direction.INPUT
pin.pull = Pull.UP

press_start_time = None

time.sleep(0.5)

while True:
	if not pin.value:
		if press_start_time is None:
			print("[BUTTON PRESSED]")
			press_start_time = time.time()
	else:
		if press_start_time:
			print(f"  - held for {time.time() - press_start_time} seconds")

		press_start_time = None

	time.sleep(0.05)
