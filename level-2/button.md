# Exercise 2

Now on to something more interesting, lighting the LED from the last exercise up, but this time with a button we can press to toggle the LED on and off.

## Setup

We'll reuse the LED configuration from the last exercise, so if you're jumping ahead you'll have to head back and set that up.

Additionally, we'll be using the rotary encoder (which looks like a little knob with legs). When you click the knob on the rotary encoder down, you're activating a button inside the rotary encoder. For what its worth though, you could use any old button you wanted here, this is just for convenience since most rotary encoders will have a button as well. We'll get to the rest of the knob functionality later.

Find an empty spot on your breadboard and add the rotary encoder oriented like you see in [the button diagram](button.png). Then, jump the "GND", or ground, prong to the negative channel, and the "SW", or switch, prong to GP7 on the Pico.

Buttons can work two ways, at rest they can either be stopping the flow of current or allowing it through, and when pressed, doing the opposite. In our case, ours are always allowing current to flow, so when the button is pushed, no current is allowed through it.

## Exercise

Alright, once everything is connected, run:

`ampy run level-2/button.py`

Unlike the last two exercises (which ran the script and then exited), we're running a `while` loop this time. This is required because we want to "listen" for button presses, and to listen we need to poll at some cadence, checking the button's state each time.

Like last time, we define a pin (GP7), but this time we set it to an "input" and "pull it up". Think of this like a default value. When a pin isn't pulled up or down, it is 
"floating", meaning it can read random, but very smal, values based on electrical noise around the pin at any given time. So without doing this, there could be times where the pin reads high or low incorrectly.

With that out of the way, we can now in a loop check the value of our pin. If it reads high, we know the button is not pressed. If it reads low, we know the button is currently pressed (or unfortunately unplugged (TODO, confirm this)).

As you click and hold the button, you should get some output letting you know when you clicked, and how long you held it for.

Alright, lets find out what the rest of the knob does!
