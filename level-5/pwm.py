import board
import time
import rotaryio
import pwmio
from digitalio import DigitalInOut, Direction, Pull

# initialize the PWM LED
led = pwmio.PWMOut(board.GP15, frequency=1000)

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
		led.duty_cycle = current_encoder_position * 500

	if not pin.value:
		if press_start_time is None:
			print("[BUTTON PRESSED]")
			press_start_time = time.time()
			led.duty_cycle = 0
	else:
		if press_start_time:
			print(f"  - held for {time.time() - press_start_time} seconds")

		press_start_time = None


	time.sleep(0.05)
