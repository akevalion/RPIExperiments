from machine import Pin, I2C
from time import sleep_ms
from sh1106 import SH1106_I2C 
#from ssd1306 import SSD1306_I2C
import math

import framebuf

i2c = I2C(1, scl = Pin( 19), sda= Pin(18))
print(i2c.scan())
#oled = SSD1306_I2C(128, 64, i2c)
oled = SH1106_I2C(128, 64, i2c)

oled.rotate(True)
x = 0

def drawCircle():
    pass

x = 0
oled.fill(0)
while x < 140:
    x += 1
    y = math.sin(math.radians(x*10))
    y = int(y * 10 + 40) 
    
    oled.pixel(x, y, 1)
    oled.show()
oled.fill(0)
oled.show()
    
    
    