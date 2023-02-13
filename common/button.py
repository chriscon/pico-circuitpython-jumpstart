from digitalio import DigitalInOut, Direction, Pull

class Button:
    def __init__(self, pin):
        self._pin = DigitalInOut(pin)
        self._pin.direction = Direction.INPUT
        self._pin.pull = Pull.UP
        self._callbacks = []

    def add_callback(self, callback):
        self._callbacks.append(callback)

    def cycle(self):
        if not self._pin.value:
            for callback in self._callbacks:
                callback()
