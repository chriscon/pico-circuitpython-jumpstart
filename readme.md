# hi

This repository is an effort to get other engineers / tinkerers / humans up-and-going with Raspberry Pi Pico boards.

After using them in a few hardware projects, I am convinced that anyone who finds writing software that interacts with hardware in the real world fascinating **needs to know** that these cheap little microcontrollers are a tool they should have in their belt.

As with most engineering, there are several different ways to get to the same end result. I am sharing the specific path I have gone down and am really enjoying, as an entrypoint into this kind of tinkering for others.

# ToC

 - [Exercise 0](level-0/board_id.md)
    - Get your local environment setup
    - Get your Pico configured
    - Run a tiny script to print the serial number for your board
 - [Exercise 1](level-1/led.md)
    - Wire in a single LED
    - Light up the LED with code
 - [Exercise 2](level-2/button.md)
    - Wire in a button to your breadboard
    - Use the button to execute code when pressed
 - [Exercise 3](level-3/rotary.md)
    - Wire in a rotary encoder
    - Use the rotary encoder to increment and decrement a value in code
 - [Exercise 4](level-4/demo.md)
    - Combine the button, rotary encoder, and LED to dynamically blink the LED
 - [Exercise 5](level-5/pwm.md)
    - Wire in a second LED
    - Use the rotary encoder to change the brightness of the new LED
 - [Exercise 6](level-6/buzzer_and_led.md)
    - Explore some of the functionality of the Maker Pi Pico
 - [Exercise 7](level-7/display.md)
    - Wire in an OLED display
    - Render text to the new display
 - [Exercise 8](level-8/complete_demo.md)
    - Combine all of the learnings to dynamically light the two LEDs via an interactive menu

# a note on the ecosystem

While you are searching around for documentation for some of the things covered in this project, you'll either find them for MicroPython or CircuitPython. CircuitPython is a fork of MicroPython which changes a small amount of things and adds some useful helpers. The full story is [here](https://learn.adafruit.com/getting-started-with-raspberry-pi-pico-circuitpython/micropython-or-circuitpython?gclid=CjwKCAiA85efBhBbEiwAD7oLQBWaJSzFVjxBunvD3ms2vhqeh-YTbKhclfUYNDCXlCngy1TPuKwSNRoCNd4QAvD_BwE).

Please be aware as you work with your Pico that some MicroPython code you find in your searching won't work when run through CircuitPython, which can make for some confusing debugging. With some wrangling, you should be able to get almost any MicroPython code to work with CircuitPython.
 
# shopping list

 Before getting started, you'll need to secure all of the materials listed out below. I am listing out my favorite places to purchase these, but you can get them from anywhere as long as you confirm they are the same or very similar. You may even need to do that, if the links die or you run into inventory issues. That said, you'll need:

### From Adafruit
 - 220Ω Resistors, from [Adafruit](https://www.adafruit.com/product/2780).
 - **[Optional, but strongly encouraged]** A Maker Pi Pico, available at [Adafruit](https://www.adafruit.com/product/5160)
   - Think of this board like a socket for your Pico. It has some real quality of life value-adds and neat functionality, and I can't overstate how great these things are for prototyping.
 - Long Breadboard, available at [Adafruit](https://www.adafruit.com/product/239)
 - Raspberry Pi Pico, available at [Adafruit](https://www.adafruit.com/product/5525). For convenience you probably want to buy one with headers already soldered on, but you absolutely can buy one without headers and solder them on yourself.
- Jumper Wires (two sets, notice the difference in the connectors), one of [these from Adafruit](https://www.adafruit.com/product/1954) and [these from Adafruit](https://www.adafruit.com/product/1955).

### From MicroCenter
 - Rotary Encoder, available at [Micro Center](https://www.microcenter.com/product/618904/KS0013_Keystudio_Rotary_Encoder_Module)

### From Amazon
 - OLED Display, available at [Amazon](https://www.amazon.com/UCTRONICS-SSD1306-Self-Luminous-Display-Raspberry/dp/B072Q2X2LL/ref=sr_1_18?crid=2ZSJ0RE12ZI2R&keywords=oled+screen+96&qid=1676087562&sprefix=oled+screenm+96%2Caps%2C68&sr=8-18)
   -  I'd prefer not to support Amazon, but they have the screen I use in this project, and I quite like this specific one. Of you'd like to shop elsewhere, you can purchase [this one](https://www.adafruit.com/product/326) from Adafruit (make sure to grab the suggested connector cable). Please note that the Adafruit screen does not have the dual monochromatic sections, see [exercise 7](level-7/display.md) for more details on that.
 - LEDs, available at [Amazon](https://www.amazon.com/DiCUNO-450pcs-Colors-Emitting-Assorted/dp/B073QMYKDM/ref=sr_1_4?crid=2K5Y1OU2WFHNM&keywords=led+pack&qid=1676088226&sprefix=led+pack%2Caps%2C92&sr=8-4)
   - Mostly any LED will work, and you only will need two.