from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(17)
plus = Button(18, bounce_time=0.05)
minus = Button(27, bounce_time=0.05)
quit = Button(22)


def increase_brightness():
	led.value = min(led.value + 0.1, 1)

def decrease_brightness():
	led.value = max(led.value - 0.1, 0)

plus.when_pressed = increase_brightness
minus.when_pressed = decrease_brightness

quit.wait_for_press()

