from machine import Pin, I2C
from time import sleep_ms
from sh1106 import SH1106_I2C
from matrix import Matrix2D
import math
import framebuf

i2c = I2C(1, scl = Pin( 19), sda= Pin(18))

print(i2c.scan())
pin = Pin(1, Pin.OUT)
pin.on()
width = 128
height = 64

oled = SH1106_I2C(width, height, i2c)

def openIcon(path):
    doc = open("wolf-pbm/"+path, "rb")
    doc.readline()
    xy = doc.readline().split()
    x = int(xy[0])
    y = int(xy[1])
    icon = bytearray(doc.read())
    doc.close()
    return framebuf.FrameBuffer(icon, x, y, framebuf.MONO_HLSB)

oled.rotate(True)
oled.fill(0)
oled.show()

x = 1
while True:
    n = str(x)
    
    image = openIcon(n + ".pbm")
    
    oled.fill(0)
    oled.blit(image, 0, 0)
    oled.show()
    sleep_ms(20)
    
    x += 1
    if x > 303:
        x = 1