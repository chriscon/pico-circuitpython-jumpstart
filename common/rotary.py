import rotaryio

class RotaryEncoder(object):
	def __init__(self, pin_a: int, pin_b: int):
		self._rotary_encoder = rotaryio.IncrementalEncoder(pin_a, pin_b)
		self._previous_encoder_position = self._rotary_encoder.position
		self._callbacks = []

	def add_callback(self, callback):
		self._callbacks.append(callback)

	def cycle(self):
		current_position = self._rotary_encoder.position
		if self._previous_encoder_position != current_position:
			direction = current_position > self._previous_encoder_position
			self._previous_encoder_position = current_position
			for callback in self._callbacks:
				callback(current_position, direction)
