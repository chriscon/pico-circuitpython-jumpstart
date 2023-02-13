import board
import time
import rotaryio
from digitalio import DigitalInOut, Direction, Pull


# initialize the LED
led = DigitalInOut(board.GP15)
led.direction = Direction.OUTPUT

def blink_led(blink_count=1):
	for blink_index in range(int(blink_count)):
		led.value = True
		time.sleep(0.1)
		led.value = False
		time.sleep(0.1)

# initialize the rotary encoder
previous_encoder_position = None
rotary_encoder = rotaryio.IncrementalEncoder(board.GP8, board.GP9)

# initialize the mementary switch
pin = DigitalInOut(board.GP7)
pin.direction = Direction.INPUT
pin.pull = Pull.UP

press_start_time = None

while True:
	current_encoder_position = rotary_encoder.position
	if current_encoder_position != previous_encoder_position:
		print(f"[ENCODER POSITION] {current_encoder_position}")
		previous_encoder_position = current_encoder_position

	if not pin.value:
		if press_start_time is None:
			print("[BUTTON PRESSED]")
			press_start_time = time.time()
			blink_led(previous_encoder_position)
	else:
		if press_start_time:
			print(f"  - held for {time.time() - press_start_time} seconds")

		press_start_time = None


	time.sleep(0.05)
