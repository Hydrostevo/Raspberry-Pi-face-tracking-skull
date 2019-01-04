from bluedot import BlueDot
from signal import pause
import os

# ServoBlaster installed and operational:
#   pi@CameraPi:~ $ cd ~/PiBits/ServoBlaster/user
#   pi@CameraPi:~/PiBits/ServoBlaster/user $ sudo ./servod
# Servo 1 (Pan) = GPIO pin 17
# Servo 2 (Tilt) = GPIO pin 18


def dpad(pos):
    if pos.top:
        command = 'echo 2=+10 > /dev/servoblaster'  # Move servo one incriment on button push
        os.system(command)
        print("Servo 2 - up")                       # Print button result in script window
    elif pos.bottom:
        command = 'echo 2=-10 > /dev/servoblaster'
        os.system(command)
        print("Servo 2 - down") 
    elif pos.left:
        command = 'echo 1=+10 > /dev/servoblaster'
        os.system(command)
        print("Servo 1 - left") 
    elif pos.right:
        command = 'echo 1=-10 > /dev/servoblaster'
        os.system(command)
        print("Servo 1 - right")
    elif pos.middle:
        command = 'echo 1=50% > /dev/servoblaster'  # Reset both servos to mid 'home' positions
        os.system(command)
        command = 'echo 2=50% > /dev/servoblaster'
        os.system(command)

bd = BlueDot()
bd.when_pressed = dpad
bd.when_moved = dpad        # Set button to work when moved not just pressed

pause()
