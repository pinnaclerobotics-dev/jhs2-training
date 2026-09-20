from pynnacle_nexus import *

# A digital input reads either HIGH (1) or LOW (0)
sensor = DigitalInput(D2)

while True:
    value = sensor.read()
    print("Digital value:", value)
    delay(200)
