from pynnacle_nexus import *

# A passive buzzer plays the frequency (in Hz) that you give it
buzzer = PassiveBuzzer(D8)

while True:
    buzzer.play(NOTE_C4)
    delay(300)
    buzzer.play(NOTE_E4)
    delay(300)
    buzzer.play(NOTE_G4)
    delay(300)

    buzzer.stop()
    delay(1000)
