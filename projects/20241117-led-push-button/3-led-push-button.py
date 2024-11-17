from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn = Button(18)

btn.when_pressed = led.on
btn.when_released = led.off

sleep(30)