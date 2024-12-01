from typing import Literal
from gpiozero import OutputDevice
from time import sleep

class Stepper4Pins:
    """
    A class to control a 4-pin stepper motor, inspired by Arduino's Stepper Library.
    
    Attributes:
        number_of_steps (int): The total number of steps for a full revolution of the stepper motor.
        step_delay (float): The delay between steps, calculated based on the RPM.
    """

    def __init__(self, number_of_steps: int, motor_pin_1: int, motor_pin_2: int, motor_pin_3: int, motor_pin_4: int):
        """
        Initializes the Stepper4Pins instance.
        
        Args:
            number_of_steps (int): The total number of steps in one revolution of the motor.
            motor_pin_1 (int): GPIO pin for motor coil A1.
            motor_pin_2 (int): GPIO pin for motor coil A2.
            motor_pin_3 (int): GPIO pin for motor coil B1.
            motor_pin_4 (int): GPIO pin for motor coil B2.
        """
        if number_of_steps <= 0:
            raise ValueError("number_of_steps must be a positive integer.")

        self.number_of_steps = number_of_steps

        self.motor_pins = [
            OutputDevice(motor_pin_1),
            OutputDevice(motor_pin_2),
            OutputDevice(motor_pin_3),
            OutputDevice(motor_pin_4),
        ]

        self.step_number = 0  
        self.set_rpm(1)       # Default RPM

        # Predefined step sequences for 4-step operation
        self.step_sequences = [
            [1, 0, 1, 0],
            [0, 1, 1, 0],
            [0, 1, 0, 1],
            [1, 0, 0, 1],
        ]

    def set_rpm(self, rpm: float):
        """
        Sets the revolutions per minute (RPM) of the stepper motor.
        
        Args:
            rpm (float): Desired RPM for the motor. Must be greater than 0.
        """
        if rpm <= 0:
            raise ValueError("RPM must be a positive value.")
        self.step_delay = 60 / self.number_of_steps / rpm

    def step(self, steps_to_move: int):
        """
        Moves the stepper motor by a specified number of steps.
        
        Args:
            steps_to_move (int): The number of steps to move. Positive for clockwise, negative for counterclockwise.
        """
        steps_remaining = abs(steps_to_move)
        direction = 1 if steps_to_move > 0 else -1

        while steps_remaining > 0:
            self.step_number = (self.step_number + direction) % self.number_of_steps
            self._set_pins(self.step_number % 4)
            steps_remaining -= 1
            sleep(self.step_delay)

    def _set_pins(self, step_index: Literal[0, 1, 2, 3]):
        """
        Activates the appropriate motor pins for the given step.
        
        Args:
            step_index (Literal[0, 1, 2, 3]): Index of the step sequence to activate.
        """
        for pin, value in zip(self.motor_pins, self.step_sequences[step_index]):
            pin.value = value

