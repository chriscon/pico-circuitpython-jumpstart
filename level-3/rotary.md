# Exercise 3

We just used the rotary encoder's button component, but we didn't use the knob at all. In this exercise, we'll use the knob of the rotary encoder to detect direction and scale. Let's get started.

## Setup

Just like last time, lets leave everything from the previous steps intact. This time though, we need to add 4 new jumper wires. First, lets jump the positive and negative connections on the rotary to the corresponding positive and negative channels on your breadboard (check out [the diagram](rotary.png) if you haven't already).

This will supply the rotary encoder with 3.3v. Next we need to jump the CLK to GP8 and DT to GP9.

I do not exactly understand the naming significance of DT and CLK, but I can share that these are both sets of contact points inside of the rotary encoder. Each set is offset slightly. This allows us (by periodically checking) to know which direction the rotary encoder is moving, and by how many steps over points. I could try to explain this in more detail, but [this write up](https://circuitdigest.com/microcontroller-projects/rotary-encoder-module-interfacing-with-arduino) does a way better job than I could.

We could code up our own rotary encoder class that tracks the state of the different sets of points (and I encourage you to if that sounds fun, you have everything you need to do that at this point), but instead we'll use a package provided by CircuitPython to save time (and bugs).

It is also worth noting that rotary encoders do not preserve state across power cycles. Put another way, if you have the rotary encoder in position -100 and unplug the Pico from your computer (removing its power source), then plug it back in, the position will report as 0. This is because the rotary encoder will always initialize at position zero and adjust from there.

For setup, thats it!

## Exercise

Alright, once everything is connected, run:

`ampy run level-3/rotary.py`

This will start an infinite loop where each cycle we check the position of the rotary encoder. If it is different than the last loop, we print out the current position to `stdout`, and we start tracking how long since the last position change (so we can share that next time the position changes). Try moving the knob into the positive and then negative positions.

Neat. So we can now understand the direction of the knob, the scale of the turn, and (from the last exercise) when the knob is clicked. Thats a lot to glean from the real world into your python code!

Alright, let's combine some of these learnings!
