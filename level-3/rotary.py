import board
import time
import rotaryio

previous_encoder_position = None
rotary_encoder = rotaryio.IncrementalEncoder(board.GP8, board.GP9)

while True:
	current_encoder_position = rotary_encoder.position
	if current_encoder_position != previous_encoder_position:
		print(f"[ENCODER POSITION] {current_encoder_position}")
		previous_encoder_position = current_encoder_position

		time.sleep(0.05)
