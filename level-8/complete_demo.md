# Exercise 8

We have come a long way in these last 9 exercises. Take a moment to appreciate the small learnings from each exercise, and consider what is now possible for you to build!

Speaking of combining all of these small learnings, let's close out this project and do just that!

## Setup

We don't need to make any changes to our breadboard, everything we configured in the last exercise set us up right where we need to be to run the exercise.

## Exercise

Okay, let's run:

`ampy run level-8/complete_demo.py`

You again should see a flash of a CircuitPython splash screen. After that though, you'll see a menu!

With this menu, we're able to toggle on/off the two LEDs we have hooked up. Neat, righ? This is obviously a very trivial menu and actions, but my hope is that it illustrates how powerful this display and menu framework can be.

A note on the menu framework. There are several out there, but the one we're using in this lesson ([umenu](https://github.com/plugowski/umenu), read as "micro menu" because it was built for MicroPython) is my favorite. I have adjusted it to work with CircuitPython in a local copy of the library included in this repo (and plan to get this update into the original library). This library has some great foundational structures I encourage you to explore, one of which is the [ValueItem](https://github.com/plugowski/umenu#valueitem) which provides a UI for adjusting an integer value up or down. If you want to take this demo further, try adding another menu item that uses PWM (which we looked at in exercise 5) and a `ValueItem` to adjust the brightness of one of the LEDs.

If we look at the code, we can see that up top we initialize our rotary encoder, a button, our display, and our two LEDs. Old news!

Then, we initialize a micro-menu into our display, with some options around how menus are displayed on our specific screen. We then initialize a menu screen and include two `ConfirmItem`s, one for each LED. Looking closer, we also provide a second argument to each `ConfirmItem` which is a method to run any time a `ConfirmItem` is positively confirmed. We could define these functions elsewhere and add them in here (making sure not to invoke them in the argument!), but as a shorthand we're using a `lambda` to define a function on the fly. Check them out if they're new to you!

The rest of this script where we define callbacks and setup an infinite loop should look very familiar from our recent exercises.

And with that, we've pulled together some very simple primatives to build something that is _still simple_ but very powerful. My hope is that you will recombine these primitives into endless new and cool combinations!

Where to next, you might ask. Your pico so far has only been powered by your computer, but it can be powered by any source that provides between 1.8 and 5.5 volts (this will include most USB power bricks you may have sitting around, but please check before using one! Over powering _and under_ powering can damange and ruin your Pico!). This even includes using batteries, which can make your project completely mobile!

All you will need to do is configure your entrypoint into your code. Similar to how we run a single file at the command line as an entrypoint (but can call into any other file we include), we can configure a sort of "autorun" entrypoint by naming a file placed on the Pico named one of `code.txt`, `code.py`, `main.txt` and `main.py`. The firmware on the Pico will try to find the first file in the ordered list above, and if one is foud, it executes it. Thats it! Thats all you need!
