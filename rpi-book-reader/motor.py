"""Module defining Motor class and related functions.

Uses Google Python Style Guide: https://google.github.io/styleguide/pyguide.html
"""

from RpiMotorLib import RpiMotorLib

class Motor:
    """Represents a Nema 23 stepper motor driven by an A4988 stepper motor driver.

    Attributes:
        PIN_DIR: An integer indicating the GPIO pin number connected to "DIR" pin
                    on the A4988 stepper motor driver.
        PIN_STEP: An integer indicating the GPIO pin number connected to "STEP"
                    pin on the A4988 stepper motor driver.
        GPIO_PINS: An tuple of three integers indicating the GPIO pin numbers that are
                    connected to MS1, MS2, and MS3 on the A4988 stepper motor driver.
    """

    def __init__(self, PIN_DIR, PIN_PUL, GPIO_PINS):
        """Initializes Motor object using RPiMotorLib library."""
        A4988Nema(PIN_DIR, PIN_STEP, GPIO_PINS)

    
