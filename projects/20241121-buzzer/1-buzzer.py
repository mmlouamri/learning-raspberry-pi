from gpiozero import Buzzer
from time import sleep # improvement -> from signal import pause

buzz = Buzzer(17)

buzz.on()
sleep(0.5)
buzz.off()
sleep(0.5)

buzz.beep() # equivalent of LED.blink

sleep(7) # improvement -> pause()
