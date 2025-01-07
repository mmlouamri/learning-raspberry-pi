from gpiozero import DistanceSensor, LED
from time import sleep

ds = DistanceSensor(echo=17, trigger=27)
green = LED(23)
yellow = LED(22)
red = LED(18)

try:
	while True:
		distance = ds.distance * 100
		print(f"Distance: {distance:.2f} cm")
		if  distance < 10:
			green.off()
			yellow.off()
			red.on()
		elif distance < 20:
			green.off()
			yellow.on()
			red.off()
		else:
			green.on()
			yellow.off()
			red.off()
		sleep(1)
except KeyboardInterrupt:
	print("Exiting...")
