from pynnacle_nexus import *

# An analog input reads a value from 0 to 1023
potentiometer = AnalogInput(A0)

while True:
    value = potentiometer.read()
    print("Analog value:", value)
    delay(200)
