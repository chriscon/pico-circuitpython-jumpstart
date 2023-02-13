# Exercise 7

We've spent a bunch of time working with inputs, but outside of blinking LEDs and writing to `stdout`, we haven't really made any meaningful outputs.

Enter, the OLED display. In this exercise, we will light up monochrome pixels in an OLED display and display some simple text to the screen.

Don't worry, the final exercise will have you writing much more interesting things to this screen. But before we get there, let's get started with the basics!

## Setup

Grab that 128x64 pixel OLED screen and place it on your breadboard similar to how we have it placed in [this diagram](display.png). We'll need to jump the positive and negative pins to the positive and negative channels on our breadboard. After that, we'll need to jump the SCL pin to GP5 and the SDA pin to GP4.

Thats all we need to hook up here. This screen uses a protocol called "I2C". For a brief introduction to I2C, read more [here](https://learn.adafruit.com/i2c-addresses?view=all&gclid=Cj0KCQiAiJSeBhCCARIsAHnAzT8ipQGXStd0CGdDRsZa2WusAYWUCyeJQ4bs1tAwGWX21tvbAAvInUAaAnjxEALw_wcB). I2C stands for inter-integrated circuit communication (engineers getting clever with their names), which has some cool benefits like only requiring two data connection wires (besides the standard positive and negative connections), and also supporting up to 128 devices using the same two wire connection.

This means we could have up to 128 devices hooked up to the same two pins on our microcontroller. This is the unrealistic upper bound, because each device specifies its own address, but duplicate components usually use the same hardware address. This means (generally) that we could only use one of our OLED screens we're using on the same two data wires, since they all identify via the same hardware address 0x3C (there are workarounds here, but I am just trying to instill awareness of a practical limitation).

## Exercise

Let's run:

`ampy run level-7/display.py`

You should see a flash of a CircuitPython splash screen and then the text "chonus" displayed. We should be able to disable this splash screen, but I will leave that as an exercise for you!

Nice! Now we can debug to a screen, draw and animate sprites, build out a menu. So many neat things unlocked!

We can see, looking at the code, that there are atributes we can change about the label we added, like the x/y position, padding, the font. On a multi-color screen we could change the text color and the background color, but because we're using a monochromatic screen, we only have "on" or "off", which we express via black and white hex codes.

A note on the monochromatic screens we're using. When you start displaying more information around the whole screen, you'll notice that the top 1/4 of the screen is a yellow/orange color, opposite the blue rest of the screen. This is a feature of the screen, where 1/4 of it is a different, but static color. We can be clever about how we display and design information on this screen to "fake" using multiple colors, while still taking advantage of the very simple and low power screen.

We can also see that we're using a `displayio.Group` to append out `label.Label` to. This is a core concept of using CircuitPython's `displayio` framework. I will admit, I don't yet have a good handle on how it all works, but I gather that it is designed this way to support effecient, but complex rendering of animations and sprites. I encourage you to do as I plan to, and read more in-depth through [this excellent guide](https://learn.adafruit.com/circuitpython-display-support-using-displayio/library-overview) from Adafruit.

Lastly, you'll see that we enter an infinite `while` loop with a small sleep. If we remove that and re-run the script, you'll see "chonus" flash on the screen briefly after the splash screen, then it will disappear. When the script we're running stops executing, the display gets cleaned up and reset.

Okay, we're now ready to pull all this together in the next and final exercise. Let's get after it!
