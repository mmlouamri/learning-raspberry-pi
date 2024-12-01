from stepper4pins import Stepper4Pins

stepper = Stepper4Pins(32 * 64, 22, 17, 27, 18)

stepper.set_rpm(10)

stepper.step(-32 * 64)
stepper.step(32 * 64)
