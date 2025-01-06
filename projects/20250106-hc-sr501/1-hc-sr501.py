from gpiozero import MotionSensor, Buzzer
from signal import pause

pir = MotionSensor(17)
buzzer = Buzzer(18)

def motion():
	buzzer.on()
	print("DETECTED!")

def stopped():
	buzzer.off()
	print("STOPPED!")

pir.when_motion = motion
pir.when_no_motion = stopped

pause()
