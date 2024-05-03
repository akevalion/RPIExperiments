from machine import Pin
from utime import sleep

red = Pin(16, Pin.OUT)
green = Pin(17, Pin.OUT)
blue = Pin(15, Pin.OUT)
 
time = 2
decay = 0.80
while True:
    red.on()
    sleep(time)
    red.off()
    green.on()
    sleep(time)
    green.off()
    blue.on()
    sleep(time)
    blue.off()
    
    time *= decay
    if time < 0.02:
        time = 2
        
