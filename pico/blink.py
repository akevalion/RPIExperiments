from machine import Pin, Timer
from utime import sleep

led = Pin(25, Pin.OUT)
red = Pin(16, Pin.OUT)
buzzer = Pin(14, Pin.OUT)

timer = Timer()
timer2 = Timer()

def blink(timer):
    led.toggle()
    
def beep(timer):
    buzzer.toggle()
    
timer.init(freq=20, mode=Timer.PERIODIC, callback=blink)
timer2.init(freq=10, mode=Timer.PERIODIC, callback=beep)

while True:
    red.toggle()
    sleep(0.5)