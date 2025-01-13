from gpiozero import Motor
from time import sleep

fl = Motor(17, 18)
fr = Motor(27, 22)
bl = Motor(23, 24)
br = Motor(9, 25)

fl.forward()
fr.forward()
sleep(0.1)
bl.forward()
br.forward()

sleep(1)

fl.stop()
fr.stop()
bl.stop()
br.stop()
