# Exercise 1

In this short exercise, we're going to do the "hello world" of hardware, lighting up an LED.

## Setup

Aside from your Pico, you'll need an LED and a resistor, in the 220Ω range.

Looking at [the board diagram](led.png), we'll need to plug or jump the shorter negative leg into the negative channel on the breadboard. Then we'll need to connect the other positive leg of the LED to GP15 on the Pico, but we need to put that 220Ω resistor between the Pico and the LED.

This is because we only want to allow 220Ω of current to get through to the LED. Without this protection, we could burn out the LED.

## Exercise

If you run the example via:

`ampy run level-1/led.py`

You should see your LED light up.

Looking at the code, we can see that we define a "pin" using `digitalio`. Think of the pin like an interface to whatever is hooked up to the Pico at that location. The interface can only understand two values, "high" and "low", and can only either read those values in or output them out, not both. In this case, "low" means no meaningful voltage is emitted, and "high" means ~3.3 volts are emitted.

So knowing that, what we do after defining the pin is set its "direction" to "output", meaning we plan to either emit a low value (no current), or a high value (~3.3v current). We then set its "value" to true, meaning set it "high". By doing that, we allow 3.3v to pass through the resistor and on to the LED, lighting it up.

And thats it, "hello world" but with an LED!
