from machine import Pin, Timer
from utime import sleep

button = Pin(14, Pin.IN, Pin.PULL_DOWN)
red = Pin(16, Pin.OUT)
led = Pin(25, Pin.OUT)

timer = Timer()

def blink(pin):
    red.toggle()
    timer.deinit()
    
def blink2(timer):
    led.toggle()

timer.init(freq=10, mode=Timer.PERIODIC, callback=blink2)

button.irq(blink, Pin.IRQ_FALLING | Pin.IRQ_RISING )