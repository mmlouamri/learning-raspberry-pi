from gpiozero import MotionSensor, Buzzer
from signal import pause
from time import sleep

pir = MotionSensor(17)
buzzer = Buzzer(18)

buzzer.on()
sleep(1)
buzzer.off()

def motion():
	buzzer.on()
	print("DETECTED!")

def stopped():
	buzzer.off()
	print("STOPPED!")

pir.when_motion = motion
pir.when_no_motion = stopped

pause()
