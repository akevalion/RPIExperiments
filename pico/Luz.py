from machine import Pin
import utime
luz=Pin(25,Pin.OUT)
luz.on()
tiempo=1000
while tiempo>0:
    luz.on()
    utime.sleep_ms(tiempo)
    luz.off()
    utime.sleep_ms(tiempo)
    tiempo=int(tiempo*0.9)
    
    
    
    