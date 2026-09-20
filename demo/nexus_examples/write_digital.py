from pynnacle_nexus import *

# A digital output can be turned on (HIGH) or off (LOW)
led = DigitalOutput(D13)

while True:
    led.on()
    delay(500)
    led.off()
    delay(500)
