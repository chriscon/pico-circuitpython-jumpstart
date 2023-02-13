import busio
import board
import displayio
import adafruit_displayio_ssd1306
from adafruit_display_text import label
from adafruit_display_shapes.rect import Rect
from adafruit_bitmap_font import bitmap_font


class Display(object):
	BOOL_TO_HEX_MAP = {
		0: 0x000000,
		1: 0xFFFFFF,
	}

	def __init__(self, device_address=0x3c, width=128, height=64):
		self.width = width
		self.height = height
		self.font = bitmap_font.load_font("/lib/common/fonts/t0-12b-uni.bdf")

		displayio.release_displays()
		_i2c = busio.I2C(scl=board.GP5, sda=board.GP4)
		display_bus = displayio.I2CDisplay(
			_i2c,
			device_address=device_address,
		)
		self._display = adafruit_displayio_ssd1306.SSD1306(
			display_bus,
			width=width,
			height=height,
		)
		self._core_group = displayio.Group()

	@property
	def palette(self):
		palette = displayio.Palette(2)
		palette[0] = 0x000000
		palette[1] = 0xFFFFFF

		return palette

	def fill(self, color_value: int):
		self.fill_rect(0, 0, self.width, self.height, background_color=color_value)

	def hline(self, x_pos, y_pos, width, color):
		self.fill_rect(x_pos, y_pos, width, 1, background_color=color)

	def text(self, text_value, x_pos, y_pos, color):
		text_area = label.Label(
			self.font,
			text=text_value,
			color=self.BOOL_TO_HEX_MAP[color],
			background_color=self.BOOL_TO_HEX_MAP[0 if color else 1], # opposite background color
			x=x_pos + 4,
			y=y_pos + 4,
			scale=1,
		)
		self._core_group.append(text_area)

	def fill_rect(self, x_pos, y_pos, width, line_height, background_color=0):
		background_rectangle = Rect(
			x_pos,
			y_pos,
			width,
			line_height,
			fill=self.BOOL_TO_HEX_MAP[background_color],
		)
		self._core_group.append(background_rectangle)

	def show(self):
		if len(self._core_group) <= 0:
			self.fill(0)

		self._display.show(self._core_group)

	def reset(self):
		self._core_group = displayio.Group()
