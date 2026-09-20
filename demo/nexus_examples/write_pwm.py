from pynnacle_nexus import *

# A PWM output takes a value from 0 to 255 (use pins marked with ~: 3, 5, 6, 9, 10, 11)
led = PwmOutput(D9)

while True:
    # Fade in
    for brightness in range(0, 256, 5):
        led.write(brightness)
        delay(20)

    # Fade out
    for brightness in range(255, -1, -5):
        led.write(brightness)
        delay(20)
