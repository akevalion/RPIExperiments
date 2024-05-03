from machine import Pin, PWM
import time

servo = PWM(Pin(0))
servo.freq(50)

led = PWM(Pin(25))
led.freq(1000)
while True:
    print("0 grados")
    servo.duty_u16(1311)
    led.duty_u16(0)
    time.sleep(2)
    
    print("180 grados")
    servo.duty_u16(7864)
    led.duty_u16(65000)
    time.sleep(2)