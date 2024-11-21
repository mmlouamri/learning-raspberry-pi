from gpiozero import PWMLED, Button
from time import sleep

led = PWMLED(17)
quit = Button(22)

led.value = 1
sleep(3)
led.value = 0.75
sleep(3)
led.value = 0.5
sleep(3)
led.value = 0.25
sleep(3)
led.value = 0

quit.wait_for_press()

