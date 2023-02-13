from digitalio import DigitalInOut, Direction, Pull

class LED:
    def __init__(self, pin: int):
        self._pin = DigitalInOut(pin)
        self._pin.direction = Direction.OUTPUT
        self.off()

    def on(self):
        self._pin.value = True

    def off(self):
        self._pin.value = False

    def toggle(self):
        self._pin.value = not self._pin.value
