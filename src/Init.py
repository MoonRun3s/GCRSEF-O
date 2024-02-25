# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# Simple test for using adafruit_motorkit with a DC motor

import time
import board
from adafruit_motorkit import MotorKit

kit = MotorKit(i2c=board.I2C())
kit.motor1.throttle = 1.0
kit.motor2.throttle = 1.0
kit.motor3.throttle = 1.0
kit.motor4.throttle = 1.0

### or...

kit.stepper1.onestep()
kit.stepper2.onestep()
