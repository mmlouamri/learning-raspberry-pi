from gpiozero import LED, Button
from time import sleep

led = LED(17)
btn = Button(18, bounce_time=0.05)

btn.when_pressed = led.toggle
btn.when_held = led.blink

sleep(30)