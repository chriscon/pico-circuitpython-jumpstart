import time
import board
from common import umenu
from common.display import Display
from common.button import Button
from common.led import LED
from common.rotary import RotaryEncoder


rotary_encoder = RotaryEncoder(board.GP8, board.GP9)
button = Button(board.GP7)
display = Display()
led_1 = LED(board.GP15)
led_2 = LED(board.GP14)

_menu = umenu.Menu(display, per_page=3, line_height=14)
_menu.set_screen(
    umenu.MenuScreen(
        "LED CONTROL"
    ).add(
		umenu.ConfirmItem(
            "LED 1",
            lambda: led_1.toggle(),
            question="Toggle LED 1?"
        )
    ).add(
		umenu.ConfirmItem(
            "LED 2",
            lambda: led_2.toggle(),
            question="Toggle LED 2?"
        )
    )
)

_menu.draw()

def menu_update_callback(current_position, direction):
	direction_is_positive = direction == True
	_menu.move(1 if direction_is_positive else -1)

rotary_encoder.add_callback(menu_update_callback)
button.add_callback(lambda: _menu.click())


while True:
	time.sleep(0.05)
	rotary_encoder.cycle()
	button.cycle()
