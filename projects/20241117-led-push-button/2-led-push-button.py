from gpiozero import LED, Button

led = LED(17)
btn = Button(18)

while True:
    btn.wait_for_press()
    led.on()
    btn.wait_for_release()
    led.off()