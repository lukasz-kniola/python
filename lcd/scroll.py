import RPi_I2C_driver
from time import *

mylcd = RPi_I2C_driver.lcd()

mylcd.lcd_clear()

mylcd.lcd_display_string("Enter text",1)
mylcd.lcd_display_string("to display.",2)

text = input("Enter text to display: ")
text = text + " "

mylcd.lcd_clear()

for row in range(1,5):
    for col in range(0,20):
        mylcd.lcd_display_string_pos(text[(((row-1)*20)+col)%len(text)],row,col)
        sleep(0.12)
