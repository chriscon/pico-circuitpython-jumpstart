# Exercise 6

Ideally, if you're working through these exercises, you were able to score a [maker pi pico base](https://www.adafruit.com/product/5160), which has some neat bells and whistles we're going to look at.

If you weren't able to score one, skip this exercise and come back when you have one. Trust me, they are worth picking up!

Otherwise, in this exercise we're going to toy with the neat multicolor LED installed on the maker pi pico base board, as well as a buzzer!

A side note, there are other interesting things on the maker pi pico board (like the MicroSD card interface and the audio jack!), but I have chosen not to cover them here. Check them out yourself though!

## Setup

There is no setup required here, you just need to ensure that you Pico is installed in the maker pi Pico board!

## Exercise

First, lets check out the multicolor LED.

Let's run the following:

`ampy run level-6/led.py`

You should see the onboard LED change to a random color every 0.1 second. Its pretty bright, right?

If you look at the code, we're using a wrapper for the "NeoPixel". In a while loop (with a short sleep) we're providing 3 random integers in the range 0-255 to an instance of the onboard LED. Those that are familiar with RGB values might be seeing whats happening here. Read on if not (read on either way lol)!

Essentially what we have on the board are three LEDs (red, green, and blue) and a little controller circuit. With those three colors, we can generate a large range of colors by turning them on (and off) in different brightnesses. Super cool, right?

If you want to read more about the NeoPixels, check [this out](https://learn.adafruit.com/adafruit-neopixel-uberguide/the-magic-of-neopixels).

Okay, let's check out that buzzer. Buzzers are all over the place in our day-to-day lives, and I have a hefty appreciation for engineers that can program pleasant sounding noises to come out of them, because I have never been able to.

Let's run:

`ampy run level-6/buzzer.py`

You should hear 7 different notes in a quick order. Looking at the code, you can see that we're using PWM again (remember that we used PWM in the last exercise to light an LED at different brightnesses). This time though, we're altering the frequency of pulses, versus altering the duty cycle. We set the duty cycle to 100%, but by changing the frequency (number of times we emit a pulse per second), we can alter the sound our ears percieve (down to the specific note!).

Again, with another link, here are some brief words about what a [piezo buzzer](https://learn.adafruit.com/using-piezo-buzzers-with-circuitpython-arduino?view=all) is. For the TL;DR; crew, in each buzzer (including the one on you maker pi pico), there is a little piezo crystal inside the buzzer that changes shape slightly when given a voltage. I know, this seems like magic, and I am pretty sure that it is. Remember that the frequency in hertz is how many times per second the duty cycle is "on" or "high"? In this case, that corresponds to how many times the crystal is given a voltage, which in turn corresponds to how many times per second the crystal quickly changes shape and then back to its resting shape.

The result, like the link above shares, is that given a specific frequency of pulses, the crystal will push up against a diaphram and emit a specific tone.

Alright, no we can make an emotional light scene with our NeoPixel and we can make some slappin' gameboy beats.

Next, lettuce move on to the most powerful component yet for humans, _the screen_.
