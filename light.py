import wiringpi
DeskState = open("state_of_pins.txt", "r+")


#Pin Array is the the state of the pins, we use it to reset the pins after we fade for startup or for wake word
#[front red, front blue, front green, back red, back blue, back green]
pinArray = [0,0,0,0,0,0] 

#give pin numbers (the set up I run uses the GPIO pin numbering )
red_front = 16
green_front = 20
blue_front = 27

red_back = 22
green_back = 21
blue_back = 17

wiringpi.wiringPiSetupGpio() #this comand tells the program to use the GPIO pinout

#these comands set up each pin as outputs
# 1 = output 0 = input
wiringpi.pinMode(red_back, 1)
wiringpi.pinMode(blue_back, 1)
wiringpi.pinMode(green_back, 1)
wiringpi.pinMode(red_front, 1)
wiringpi.pinMode(blue_front, 1)
wiringpi.pinMode(green_front, 1)

#thest comands create the ablity for PWM on each pin with the range of each
wiringpi.softPwmCreate(red_front, 0, 100)
wiringpi.softPwmCreate(blue_front, 0, 100)
wiringpi.softPwmCreate(green_front, 0, 100)
wiringpi.softPwmCreate(red_back, 0, 100)
wiringpi.softPwmCreate(blue_back, 0, 100)
wiringpi.softPwmCreate(green_back, 0, 100)

#global variables to replace 0 and 1 where needed
ON = 100
OFF = 0

def writepins():
    for state in pinArray:
    DeskState.write(state)
    DeskState.write("\n")


def resetpins():
    wiringpi.softPwmWrite(red_front, pinArray[0])
    wiringpi.softPwmWrite(blue_front, pinArray[1])
    wiringpi.softPwmWrite(green_front, pinArray[2])
    wiringpi.softPwmWrite(red_back, pinArray[0])
    wiringpi.softPwmWrite(blue_back, pinArray[1])
    wiringpi.softPwmWrite(green_back, pinArray[2])





def setup():
    wiringpi.wiringPiSetupGpio()

    wiringpi.pinMode(red_back, 1)
    wiringpi.pinMode(blue_back, 1)
    wiringpi.pinMode(green_back, 1)
    wiringpi.pinMode(red_front, 1)
    wiringpi.pinMode(blue_front, 1)
    wiringpi.pinMode(green_front, 1)

    wiringpi.softPwmCreate(red_front, 0, 100)
    wiringpi.softPwmCreate(blue_front, 0, 100)
    wiringpi.softPwmCreate(green_front, 0, 100)
    wiringpi.softPwmCreate(red_back, 0, 100)
    wiringpi.softPwmCreate(blue_back, 0, 100)
    wiringpi.softPwmCreate(green_back, 0, 100)

#color functions----------------------------------------


def white(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def red(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, OFF)
    wiringpi.softPwmWrite(blue, OFF)
def blue(red,blue,green):
    wiringpi.softPwmWrite(red, OFF)
    wiringpi.softPwmWrite(green, OFF)
    wiringpi.softPwmWrite(blue, ON)
def green(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def yellow(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def purple(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def teal(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
#----------------------------------------------------
#-----------turn off lights function
def off(location):
    setup()
    if location == "FRONT LIGHTS":
        red_off = red_front
        blue_off = blue_front
        green_off = green_front
    if location == "BACK LIGHTS":
        red_off = red_back
        blue_off = blue_back
        green_off = green_back
    if location == "BOTH LIGHTS":
        GPIO.output(red_front, GPIO.LOW)
        GPIO.output(green_front, GPIO.LOW)
        GPIO.output(blue_front, GPIO.LOW)
        red_off = red_back
        blue_off = blue_back
        green_off = green_back
    GPIO.output(red_off, GPIO.LOW)
    GPIO.output(green_off,GPIO.LOW)
    GPIO.output(blue_off,GPIO.LOW)
#----------set color fucntion
def set(location, color):
    if location == "FRONT LIGHTS":
        if color == "red":
            red(red_front, blue_front, green_front)
            pinArray[0] = ON
            pinArray[1] = OFF
            pinArray[2] = OFF
        elif color == "blue":
            blue(red_front, blue_front, green_front)
            pinArray[0] = OFF
            pinArray[1] = ON
            pinArray[2] = OFF
        elif color == "green":
            green(red_front, blue_front, green_front)
            pinArray[0] = OFF
            pinArray[1] = OFF
            pinArray[2] = ON
        elif color == "purple":
            purple(red_front, blue_front, green_front)
            pinArray[0] = ON
            pinArray[1] = ON
            pinArray[2] = OFF
        elif color == "white":
            white(red_front, blue_front, green_front)
            pinArray[0] = ON
            pinArray[1] = ON
            pinArray[2] = ON
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
            pinArray[0] = ON
            pinArray[1] = OFF
            pinArray[2] = ON
        elif color == "teal":
            teal(red_front, blue_front, green_front)
            pinArray[0] = 0
            pinArray[1] = 1
            pinArray[2] = 1
    elif location == "BACK LIGHTS":
        if color == "red":
            red(red_back, blue_back, green_back)
            pinArray[3] = 1
            pinArray[4] = 0
            pinArray[5] = 0
        elif color == "blue":
            blue(red_back, blue_back, green_back)
            pinArray[3] = 0
            pinArray[4] = 1
            pinArray[5] = 0
        elif color == "green":
            green(red_back, blue_back, green_back)
            pinArray[3] = 0
            pinArray[4] = 0
            pinArray[5] = 1
        elif color == "purple":
            purple(red_back, blue_back, green_back)
            pinArray[3] = 1
            pinArray[4] = 1
            pinArray[5] = 0
        elif color == "white":
            white(red_back, blue_back, green_back)
            pinArray[3] = 1
            pinArray[4] = 1
            pinArray[5] = 1
        elif color == "yellow":
            yellow(red_back, blue_back, green_back)
            pinArray[3] = 1
            pinArray[4] = 0
            pinArray[5] = 1
        elif color == "teal":
            teal(red_back, blue_back, green_back)
            pinArray[3] = 0
            pinArray[4] = 1
            pinArray[5] = 1
    elif location == "BOTH LIGHTS":
        if color == "red":
            red(red_front, blue_front, green_front)
            red(red_back, blue_back, green_back)
            pinArray = [1,0,0,1,0,0]
        elif color == "blue":
            blue(red_front, blue_front, green_front)
            blue(red_back, blue_back, green_back)
            pinArray = [0,1,0,0,1,0]
        elif color == "green":
            green(red_front, blue_front, green_front)
            green(red_back, blue_back, green_back)
            pinArray = [0,0,1,0,0,1]
        elif color == "purple":
            purple(red_front, blue_front, green_front)
            purple(red_back, blue_back, green_back)
            pinArray = [1,1,0,1,1,0]
        elif color == "white":
            white(red_front, blue_front, green_front)
            white(red_back, blue_back, green_back)
            pinArray = [1,1,1,1,1,1]
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
            yellow(red_back, blue_back, green_back)
            pinArray = [1,0,1,1,0,1]
        elif color == "teal":
            teal(red_front, blue_front, green_front)
            teal(red_back, blue_back, green_back)
            pinArray = [0,1,1,0,1,1]
#---------------------fade functions
def fade(front,back):
        for brightness in range(0,100):
            wiringpi.softPwmWrite(front, brightness)
            wiringpi.softPwmWrite(back, brightness)
            wiringpi.delay(15)
        for brightness in reversed(range(0,100)):
            wiringpi.softPwmWrite(front, brightness)
            wiringpi.softPwmWrite(back, brightness)
            wiringpi.delay(15)
