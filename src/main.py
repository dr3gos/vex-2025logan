# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main.py                                                      #
# 	Author:       dragos                                                       #
# 	Created:      1/28/2025, 3:59:01 PM                                        #
# 	Description:  V5 project                                                   #
#                                                                              #
# ---------------------------------------------------------------------------- #

# Library imports
from vex import *

# Brain should be defined by default
brain=Brain()

brain.screen.print("Hello V5")

controller_1 = Controller(PRIMARY)
leftRear = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)       
rightRear = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)       
leftFront = Motor(Ports.PORT5, GearSetting.RATIO_18_1, True)       
rightFront = Motor(Ports.PORT4, GearSetting.RATIO_18_1, False)
trapMotor = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
intakeMotor = Motor(Ports.PORT2, GearSetting.RATIO_18_1, False)
slamdunkMotor = Motor(Ports.PORT3, GearSetting.RATIO_18_1, False)
# sucker = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
# pneumatic = DigitalOut(brain.three_wire_port.a)

wait(30, MSEC)

# Functions

# Driving function

def slamdunk():
    pass
    
def intake():
    pass
    
def trap():
    pass

def move(direction, power, duration):
# 1 = forward, 2 = backward, 3 = left, 4 = right
    if direction == 1:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(REVERSE)
        leftRear.spin(REVERSE)
        rightRear.spin(REVERSE)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 2:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD)
        rightFront.spin(FORWARD)
        leftRear.spin(FORWARD)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 3:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD) #f
        rightFront.spin(REVERSE) #r
        leftRear.spin(FORWARD) #f
        rightRear.spin(REVERSE) #r
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 4:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(FORWARD)
        leftRear.spin(REVERSE)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 5:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(FORWARD)
        rightFront.spin(REVERSE)
        leftRear.spin(REVERSE)
        rightRear.spin(FORWARD)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()
    if direction == 6:
        leftFront.set_velocity(power, PERCENT)
        rightFront.set_velocity(power, PERCENT)
        leftRear.set_velocity(power, PERCENT)
        rightRear.set_velocity(power, PERCENT)

        leftFront.spin(REVERSE)
        rightFront.spin(FORWARD)
        leftRear.spin(FORWARD)
        rightRear.spin(REVERSE)
        wait(duration, MSEC)
        leftFront.stop()
        rightFront.stop()
        leftRear.stop()
        rightRear.stop()

def drivingsimple():
    speed = -controller_1.axis3.position() #updown left
    # strafe = controller_1.axis4.position() #leftright left
    turn = controller_1.axis1.position()  #leftright right

    leftRearPower = (speed - turn)
    rightRearPower = (speed + turn)

    leftRear.set_velocity(leftRearPower, PERCENT)
    rightRear.set_velocity(rightRearPower, PERCENT)

    leftRear.spin(FORWARD)
    rightRear.spin(FORWARD)

def driving():
    turn = -controller_1.axis1.position() #updown left
    speed = -controller_1.axis3.position() #leftright left
    strafe = -controller_1.axis4.position() #lefright right

    leftFrontPower = speed + turn + strafe;
    rightFrontPower = speed - turn - strafe;
    leftRearPower = speed + turn - strafe;
    rightRearPower = speed - turn + strafe;

    leftFront.set_velocity(leftFrontPower, PERCENT)
    rightFront.set_velocity(rightFrontPower, PERCENT)
    leftRear.set_velocity(leftRearPower, PERCENT)
    rightRear.set_velocity(rightRearPower, PERCENT)

    leftFront.spin(FORWARD)
    rightFront.spin(FORWARD)
    leftRear.spin(FORWARD)
    rightRear.spin(FORWARD)


# Main loop
while 1:
    if controller_1.buttonRight.pressing():
        pass
        # autonomous()
    if controller_1.buttonLeft.pressing():
        while 1:
            driving()
    wait(5, MSEC)