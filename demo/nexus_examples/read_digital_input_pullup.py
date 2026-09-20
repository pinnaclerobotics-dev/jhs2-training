from pynnacle_nexus import *

# A pull-up input uses the board's built-in resistor, so it reads HIGH (1) by default
# and LOW (0) when the connected device pulls the pin to ground
sensor = DigitalInputPullup(D2)

while True:
    value = sensor.read()
    print("Digital value:", value)
    delay(200)
