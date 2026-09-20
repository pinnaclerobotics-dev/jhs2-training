from pynnacle_nexus import *

# is_toggled() is True once per press-and-release, so holding the button doesn't repeat
button = Button(D4, NORMALLY_OPEN)
led = DigitalOutput(D13)
led_is_on = False

while True:
    if button.is_toggled():
        led_is_on = not led_is_on

        if led_is_on:
            led.on()
        else:
            led.off()

        print("LED on:", led_is_on)
