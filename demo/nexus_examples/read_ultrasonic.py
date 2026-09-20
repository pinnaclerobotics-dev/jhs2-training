from pynnacle_nexus import *

# An ultrasonic sensor needs a trigger pin and an echo pin
sensor = UltrasonicSensor(D6, D7)

while True:
    distance = sensor.read()
    print("Distance:", distance)
    delay(200)
