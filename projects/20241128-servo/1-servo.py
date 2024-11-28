from gpiozero import  Button, Servo
from time import sleep

servo = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
quit = Button(22)

servo.min()
sleep(3)
servo.max()
sleep(3)


quit.wait_for_press()




