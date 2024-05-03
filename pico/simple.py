from machine import Pin
from utime import sleep
pin1 = Pin(17, Pin.OUT)
pin2 = Pin(16, Pin.OUT)

base = 2
decay = 0.80
while True:
    pin1.low()
    pin2.high()
    sleep(base)
    base *= decay
    if base < 0.02:
        base = 2
    pinaux = pin1
    pin1 = pin2
    pin2 = pinaux