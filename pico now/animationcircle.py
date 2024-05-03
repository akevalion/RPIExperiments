from machine import Pin, I2C
from time import sleep_ms
from sh1106 import SH1106_I2C
from matrix import Matrix2D
import math
import framebuf

i2c = I2C(1, scl = Pin( 19), sda= Pin(18))

print(i2c.scan())
pin = Pin(25, Pin.OUT)
pin.on()
width = 128
height = 64
oled = SH1106_I2C(width, height, i2c)

frame = 0
step = 3.5
radius = 25
bar = 30
def drawLine(x1, y1, x2, y2):
    oled.line(int(x1), int(y1), int(x2), int(y2), 1)

while True:
    oled.fill(0)
    for i in range(0, 360, 10):
        alpha = math.radians(i)
        cos = math.cos(alpha)
        sin = math.sin(alpha)
        
        mat = Matrix2D()
        mat.translateBy(width/2, height/2)
        mat.translateBy(cos*radius, sin * radius)
        mat.rotateByRadians(alpha + alpha * step * 5 + frame * 0.02)
        
        p1 = mat.transform(bar / 2, 0)
        p2 = mat.transform(bar / -2 * cos, 0)
        
        drawLine(p1[0], p1[1], p2[0], p2[1])
        
    oled.show()
    frame += 1
    
oled.fill(0)
oled.show()