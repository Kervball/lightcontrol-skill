import wiringpi

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
ON = 1
OFF = 0

def white(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def red(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
    wiringpi.softPwmWrite(blue, ON)
def blue(red,blue,green):
    wiringpi.softPwmWrite(red, ON)
    wiringpi.softPwmWrite(green, ON)
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
        elif color == "blue":
            blue(red_front, blue_front, green_front)
        elif color == "green":
            green(red_front, blue_front, green_front)
        elif color == "purple":
            purple(red_front, blue_front, green_front)
        elif color == "white":
            white(red_front, blue_front, green_front)
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
        elif color == "teal":
            teal(red_front, blue_front, green_front)
    elif location == "BACK LIGHTS":
        if color == "red":
            red(red_back, blue_back, green_back)
        elif color == "blue":
            blue(red_back, blue_back, green_back)
        elif color == "green":
            green(red_back, blue_back, green_back)
        elif color == "purple":
            purple(red_back, blue_back, green_back)
        elif color == "white":
            white(red_back, blue_back, green_back)
        elif color == "yellow":
            yellow(red_back, blue_back, green_back)
        elif color == "teal":
            teal(red_back, blue_back, green_back)
    elif location == "BOTH LIGHTS":
        if color == "red":
            red(red_front, blue_front, green_front)
            red(red_back, blue_back, green_back)
        elif color == "blue":
            blue(red_front, blue_front, green_front)
            blue(red_back, blue_back, green_back)
        elif color == "green":
            green(red_front, blue_front, green_front)
            green(red_back, blue_back, green_back)
        elif color == "purple":
            purple(red_front, blue_front, green_front)
            purple(red_back, blue_back, green_back)
        elif color == "white":
            white(red_front, blue_front, green_front)
            white(red_back, blue_back, green_back)
        elif color == "yellow":
            yellow(red_front, blue_front, green_front)
            yellow(red_back, blue_back, green_back)
        elif color == "teal":
            teal(red_front, blue_front, green_front)
            teal(red_back, blue_back, green_back)
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
