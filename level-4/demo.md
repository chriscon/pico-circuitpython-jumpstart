# Exercise 4

Let's take a minute to combine all the things we've learned in the exercises so far. In this exercise, we will use the rotary encoder to select an integer value, and when we click the rotary encoder button, we will blink the LED from exercise 1 as many times as the integer value is set to.

Let's get to it!

## Setup

Just like last time, lets leave everything from the previous steps intact. [This is what we want to be working with](demo.png).

We actually don't have to change anything on the breadboard for this exercise! Just make sure you have everything from the previous exercises all wired up still. If you've removed LED and/or rotary encoder connections (or you jumped ahead like an ambitous nerd), just head back to exercise 1 and work back up to here.

## Exercise

Now we can do something approaching useful, run:

`ampy run level-4/demo.py`

When you move the rotary encoder, you should see the same message as the last exercise that logs the current position of the rotary encoder. But now, if you click the button on the rotary encoder with a positive current position value, you should see the LED quickly blink that same number of times. Neat, right? Let's look at what the code is doing.

We set up an LED (just like in exercise 1), but we also set up a callback function that takes in a `blink_count` argument. Inside, we see that we will blink the LED `blink_count` times, with a very short sleep in there.

A short side note, since we're not using any async programming patterns here, the evaluation of our script blocks during sleeps. What this means is that if you set the position of the rotary encoder very high, you will have to wait for all of thos 0.1 second sleeps to elapse before you can detect a new position on the rotary encoder. `asyncio` is available to use in CircuitPython, and I strongly encourage you to use it! But to keep this demo simple, I am abstaining from asynchronicity.

The rest of the code should look just like exercise 3, except we stuck a call to `blink_led` in the button press handler.

Neat stuff, right? You could almost impress friends with what we've built so far, but stick it out to the end for lasting impressions! Let's move on.
