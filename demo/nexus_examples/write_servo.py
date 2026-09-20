from pynnacle_nexus import *

# A servo motor moves to an angle from 0 to 180 degrees
servo = Servo(D10)

while True:
    servo.write(0)
    delay(1000)
    servo.write(90)
    delay(1000)
    servo.write(180)
    delay(1000)
