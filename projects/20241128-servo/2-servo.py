from gpiozero import Servo, Button
from signal import pause


btn = Button(22, bounce_time=0.05)
srv = Servo(18, min_pulse_width=0.0005, max_pulse_width=0.0025)
state_max = False
srv.min()

def toggle_srv():
	global state_max
	if state_max:
		srv.min()
	else:
		srv.max()
	state_max = not state_max

btn.when_pressed = toggle_srv

pause()
