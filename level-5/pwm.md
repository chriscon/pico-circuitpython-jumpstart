# Exercise 5

So we've made some great progress so far, let's talk about something interesting, PWM (pulse width modulation), and use it to change the brightness of our LED, using what we've learned about the rotary encoder.

## Setup

We're going to use all the connections from the previous steps (I know, I am a broken record), but we're also going to add a new LED (alongside the one we already have on the breadboard).

Grab another LED (one that is a different color than the one you already have on the breadboard), and another 220Ω resistor. Referencing [this diagram](pwm.png), jump the negative side of your LED to the negative channel on your breadboard, and jump the positive side of the LED to GP15 on the Pico, making sure that the resistor is inline between the Pico pin and the LED positive lead.

Thats it! We can now use PWM to light up this LED.

## Exercise

Let's run the following:

`ampy run level-5/pwm.py`

When you turn the rotary encoder knob, you should see the familiar `stdout` logging that tells you which position the rotary encoder is in, but as you turn it further into the positive direction, you should see your LED begin to light up, brighter and brighter as you turn.

Neat! Let's look at the code and see whats happening. We initialize the LED similar to like we did previously, but this time we use a wrapper from the `pwm` package, `pwmio.PWMOut`. This is a good time to talk about what pulse width modulation is. Again, I will link to a [better explination](https://learn.sparkfun.com/tutorials/pulse-width-modulation/all) than I can do, but I'll also give it a shot.

PWM has a concept of a "duty cycle", which I understand as for any given period of time, the duty cycle percentage is how much time the pin is spent high (given voltage). We describe this interval as hertz, events per 1 second. At initialization we set the `frequency` value to 1,000 hertz, meaning we want to pulse the output pin 1,000 times per second. At a 50% duty cycle, we would pulse a high value every other "tick", or half the time, which means the LED would appear at its half brightness value for the supplied max voltage.

This is a lot of information, but it is important to understand, at least somewhat, what we're sending out pulses of high and low values extremely quickly, and depending on how we adjust those pulses, the LED will be brigher or darker.

The duty cycle for the package we're using is a 16 bit value, so there are 65,536 values in the duty cycle range. You can see, looking at the code, that we take the position of the rotary encoder and multiply it by 500, which allows us to step through the 65,536 value range coarsely.

Okay, I know, thats a lot of words, but hopefully they have conveyed how neat and useful PWM is. You will see it used _a lot_ if you keep going down this tinkering rabbit hole.

Alright, lets have a diversion into some less useful but neat bits!
