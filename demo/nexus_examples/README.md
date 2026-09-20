# Nexus Examples

Small examples for the `pynnacle-nexus` package and the Pinnacle Nexus board. Each file runs forever in a `while True` loop; press Ctrl+C to stop.

```
pip install pynnacle-nexus
python <example_file>.py
```

| File                 | Shows how to                                     | Pin(s)               |
| -------------------- | ------------------------------------------------ | -------------------- |
| `read_digital.py`    | Read a digital input (`DigitalInput`)            | D2                   |
| `read_analog.py`     | Read an analog input, 0-1023 (`AnalogInput`)     | A0                   |
| `write_digital.py`   | Turn an LED on and off (`DigitalOutput`)         | D13                  |
| `write_pwm.py`       | Fade an LED with PWM (`PwmOutput`)               | D9                   |
| `play_buzzer.py`     | Play notes on a passive buzzer (`PassiveBuzzer`) | D8                   |
| `read_ultrasonic.py` | Measure distance (`UltrasonicSensor`)            | D6 (trig), D7 (echo) |
| `write_servo.py`     | Move a servo, 0-180 degrees (`Servo`)            | D10                  |
| `toggle_button.py`   | Detect a button press-and-release (`Button`)     | D4                   |

Change the pin in each file to match how your parts are wired.
