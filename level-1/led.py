from digitalio import DigitalInOut, Direction, Pull
import board
import time

pin = DigitalInOut(board.GP15)
pin.direction = Direction.OUTPUT

print("[LED ON]")
pin.value = True

time.sleep(5)
