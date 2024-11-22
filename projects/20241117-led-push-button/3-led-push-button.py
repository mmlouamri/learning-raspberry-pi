from gpiozero import LED, Button
from time import sleep # improvement -> from signal import pause

led = LED(17)
btn = Button(18)

btn.when_pressed = led.on
btn.when_released = led.off

sleep(30) # improvement -> pause()
