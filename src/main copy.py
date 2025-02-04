# ---------------------------------------------------------------------------- #
#                                                                              #
# 	Module:       main2.py                                                     #
# 	Project:      AISB VEX 24'-25' Unc Tyrone                                  #
# 	Author:       Dragos S.                                                    #
# 	Created:      30/01/2025                                                   #
# 	Description:  Massive optimizations                                        #
#                                                                              #
# ---------------------------------------------------------------------------- #


from vex import *

# Initialize hardware components
brain = Brain()
controller = Controller()

# Configure motors

left_motorB = Motor(Ports.PORT5, GearSetting.RATIO_18_1, False)
right_motorB = Motor(Ports.PORT6, GearSetting.RATIO_18_1, False)
left_motorF = Motor(Ports.PORT7, GearSetting.RATIO_18_1, False)
right_motorF = Motor(Ports.PORT8, GearSetting.RATIO_18_1, False)
# wheels 5 6 7 8
intake = Motor(Ports.PORT9, GearSetting.RATIO_18_1, False)
spinner = Motor(Ports.PORT10, GearSetting.RATIO_18_1, False)
trapper = Motor(Ports.PORT20, GearSetting.RATIO_18_1, False)

# Global state variables
intake_spinner_state = 0  # 0=stopped, 1=forward, 2=reverse
trapper_toggled = False
last_buttons = {
    'L2': False,
    'R2': False,
    'A': False
}

# Control modes
class Mode:
    DISABLED = 0
    AUTONOMOUS = 1
    DRIVER = 2

current_mode = Mode.DISABLED

def drive_control():
    # Arcade drive implementation


    forward = controller.axis3.position()
    turn = controller.axis1.position()
    strafe = controller.axis4.position() 

    
    leftB = turn - strafe + forward
    rightB = turn - strafe - forward
    leftF = turn + strafe + forward
    rightF = turn + strafe - forward

    left_motorB.spin(FORWARD, max(-100, min(leftB, 100)), PERCENT)
    right_motorB.spin(FORWARD, max(-100, min(rightB, 100)), PERCENT)
    left_motorF.spin(FORWARD, max(-100, min(leftF, 100)), PERCENT)
    right_motorF.spin(FORWARD, max(-100, min(rightF, 100)), PERCENT)

def intake_spinner_control():
    global intake_spinner_state, last_buttons
    
    L2 = controller.buttonL2.pressing()
    R2 = controller.buttonR2.pressing()
    
    # Toggle handling
    if L2 and not last_buttons['L2']:
        intake_spinner_state = 1 if intake_spinner_state != 1 else 0
    if R2 and not last_buttons['R2']:
        intake_spinner_state = 2 if intake_spinner_state != 2 else 0
    
    # State execution
    if intake_spinner_state == 1:
        intake.spin(FORWARD, 50, PERCENT)
        spinner.spin(FORWARD, 80, PERCENT)
    elif intake_spinner_state == 2:
        intake.spin(REVERSE, 50, PERCENT)
        spinner.spin(REVERSE, 80, PERCENT)
    else:
        intake.stop()
        spinner.stop()
    
    last_buttons['L2'] = L2
    last_buttons['R2'] = R2

def trapper_control():
    global trapper_toggled, last_buttons
    
    A = controller.buttonA.pressing()
    B = controller.buttonB.pressing()
    
    if A and not last_buttons['A']:
        trapper_toggled = not trapper_toggled
    
    if B:
        trapper.spin(REVERSE, 100, PERCENT)
    elif trapper_toggled:
        trapper.spin(FORWARD, 100, PERCENT)
    else:
        trapper.stop()
    
    last_buttons['A'] = A

def autonomous():
    # !!! Autonomous code goes here !!!
    pass
    

def driver_control():
    drive_control()
    intake_spinner_control()
    trapper_control()

def check_mode_switch():
    global current_mode
    # Switch to autonomous on left arrow press
    if controller.buttonLeft.pressing() and current_mode == Mode.DISABLED:
        current_mode = Mode.AUTONOMOUS
    # Switch to driver control on right arrow press
    elif controller.buttonRight.pressing() and current_mode == Mode.DISABLED:
        current_mode = Mode.DRIVER

def main_loop():
    global current_mode
    
    while True:
        check_mode_switch()
        
        if current_mode == Mode.AUTONOMOUS:
            autonomous()
            current_mode = Mode.DISABLED  # Return to disabled after autonomous
        elif current_mode == Mode.DRIVER:
            driver_control()
        else:
            # Stop all motors in disabled mode
            left_motorB.stop()
            right_motorB.stop()
            left_motorF.stop()
            right_motorF.stop()
            intake.stop()
            spinner.stop()
            trapper.stop()
        
        wait(20, MSEC)

# Start the program
main_loop()