import busio
import board
import displayio
import terminalio
import time
import adafruit_displayio_ssd1306
from adafruit_display_text import label


device_address = 0x3c
display_width_pixels = 128
display_height_pixels = 64
scl_pin = board.GP5
sda_pin = board.GP4

# reset any connected dislpays
displayio.release_displays()

_i2c = busio.I2C(scl=scl_pin, sda=sda_pin)
display_bus = displayio.I2CDisplay(
	_i2c,
	device_address=device_address,
)
_display = adafruit_displayio_ssd1306.SSD1306(
	display_bus,
	width=display_width_pixels,
	height=display_height_pixels,
)

_screen = displayio.Group()
_display.show(_screen)


text = "chonus"
text_area = label.Label(
	terminalio.FONT,
	text=text,
	color=0x000000,
	background_color=0xFFFFFF,
	x=44,
	y=34,
	padding_top=5,
	padding_left=5,
	padding_bottom=5,
	padding_right=5,
)
_screen.append(text_area)
_display.show(_screen)

while True:
	time.sleep(0.5)
