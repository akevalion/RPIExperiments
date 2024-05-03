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
espera = 50
oled = SH1106_I2C(width, height, i2c)
oled.rotate(True)
oled.fill(0)
def dibujarTablero():
    for fila in range(0,8):
        diferencia=0
        if fila%2==0:
            diferencia=8
        for columna in range(0,4):
            oled.fill_rect(columna*16+diferencia,fila*8,8,8, 1)

dibujarTablero()
oled.text('Rogelio', 70, 10, 1)
#oled.text('Milton', 70, 20, 1)
#oled.text(':)', 70, 30, 1)
oled.show()