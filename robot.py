# Simple demo of of the PCA9685 PWM servo/LED controller library.
# This will move channel 0 from min to max position repeatedly.
# Author: Tony DiCola
# License: Public Domain
from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
import argparse
ap = argparse.ArgumentParser()
ap.add_argument("-n", required = True, help = "Path to the image")
args = vars(ap.parse_args())
n = args["n"]


# Uncomment to enable debug output.
#import logging
#logging.basicConfig(level=logging.DEBUG)

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685()

# Alternatively specify a different address and/or bus:
#pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

# Configure min and max servo pulse lengths
servo_min = 150  # Min pulse length out of 4096
servo_max = 300  # Max pulse length out of 4096

# Helper function to make setting a servo pulse width simpler.
def set_servo_pulse(channel, pulse):
    pulse_length = 1000000    # 1,000,000 us per second
    pulse_length //= 60       # 60 Hz
    print('{0}us per period'.format(pulse_length))
    pulse_length //= 4096     # 12 bits of resolution
    print('{0}us per bit'.format(pulse_length))
    pulse *= 1000
    pulse //= pulse_length
    pwm.set_pwm(channel, 0, pulse)

pwm.set_pwm(2, 0, 0)
pwm.set_pwm(1, 0, 0)
pwm.set_pwm(0, 0, 0)

# Set frequency to 60hz, good for servos.
pwm.set_pwm_freq(10)

print('Moving servo on channel 0, press Ctrl-C to quit...')
    # Move servo on channel O between extremes.
time.sleep(3)
def cha_0() :
    #pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(2, 0, 130)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 200)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 190)
    #pwm.set_pwm(1, 0, servo_max)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 130)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 200)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 200)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(1)

def cha_1() :
    #pwm.set_pwm(2, 0, 200)
    pwm.set_pwm(2, 0, 180)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 220)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 180)
    #pwm.set_pwm(1, 0, servo_max)
    time.sleep(1)

    # sec cha
    #pwm.set_pwm(2, 0, 190)
    pwm.set_pwm(2, 0, 170)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 190)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 250)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(1)

def cha_2() :
    pwm.set_pwm(2, 0, 250)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 300)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 190)
    #pwm.set_pwm(1, 0, servo_max)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 250)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 180)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 300)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    time.sleep(1)

def cha_3() :
    #pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(2, 0, 130)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 200)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 180)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

    # sec cha
    #pwm.set_pwm(2, 0, 150)
    pwm.set_pwm(2, 0, 130)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 180)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 190)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 190)
    time.sleep(1)

def cha_4() :
    pwm.set_pwm(2, 0, 150)
    #pwm.set_pwm(2, 0, 190)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 200)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 200)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 180)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 250)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 180)
    time.sleep(1)

def cha_5() :
    pwm.set_pwm(2, 0, 230)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 200)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 260)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 200)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 300)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 190)
    time.sleep(1)

def cha_6() :
    pwm.set_pwm(2, 0, 150)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 180)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 140)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    pwm.set_pwm(1, 0, 160)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 148)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 180)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

def cha_7() :
    #pwm.set_pwm(2, 0, 180)
    pwm.set_pwm(2, 0, 160)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 180)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    #pwm.set_pwm(1, 0, 150)
    pwm.set_pwm(1, 0, 140)
    time.sleep(1)

    # sec cha
    pwm.set_pwm(2, 0, 140)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 160)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 200)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

def cha_8() :
    #pwm.set_pwm(2, 0, 200)
    pwm.set_pwm(2, 0, 215)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(3)
    # sec line
    pwm.set_pwm(2, 0, 220)
    time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    time.sleep(0.1)
    #pwm.set_pwm(1, 0, 140)
    pwm.set_pwm(1, 0, 135)
    time.sleep(1)

    # sec cha
    #pwm.set_pwm(2, 0, 180)
    pwm.set_pwm(2, 0, 215)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 150)
    time.sleep(3)
    #pwm.set_pwm(1, 0, 0)
    # sec line
    pwm.set_pwm(2, 0, 260)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 170)
    time.sleep(1)

def test() :
    pwm.set_pwm(0, 0, 100)
    for i in range(1,6) :
        if (i == 5) :
            print(100)
            pwm.set_pwm(1, 0, 100)
            time.sleep(1)
        else :
            print(servo_min + i*100)
            pwm.set_pwm(1, 0, servo_min + i*100)
            time.sleep(1)
    pwm.set_pwm(1, 0, 0)
    
def test1() :
    pwm.set_pwm(0, 0, 150)
    time.sleep(1)
    pwm.set_pwm(0, 0, 0)

def test2() :
    pwm.set_pwm(2, 0, 500)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 150)
    #time.sleep(0.1)
    pwm.set_pwm(1, 0, 220)
    """pwm.set_pwm(1, 0, 200)
    #time.sleep(0.1)
    pwm.set_pwm(0, 0, 150)
    time.sleep(3)"""

def test3() :
    start=150
    pwm.set_pwm(1, 0, 220)
    for i in range(15) :
        pwm.set_pwm(0, 0, start)
        print(start)
        start += 30
        time.sleep(1)
    #pwm.set_pwm(1, 0, 220)
    #time.sleep(0.1)
    #pwm.set_pwm(0, 0, 100)
    #time.sleep(0.1)
    #pwm.set_pwm(1, 0, 180)
    time.sleep(0.5)

def dance() :
    start=150
    zero = 150
    two = 550
    for i in range(8) :
        """if i % 3 == 0 :
            pwm.set_pwm(2, 0, 550)
        elif i % 3 == 1 :
            pwm.set_pwm(2, 0, 520)
        elif i % 3 == 2 :
            pwm.set_pwm(2, 0, 600)
        else :
            pwm.set_pwm(2, 0, 580)"""
        pwm.set_pwm(2, 0, two)
        #pwm.set_pwm(1, 0, start)
        pwm.set_pwm(0, 0, zero)
        print(start)
        start += 30
        if i % 2 == 0 :
            zero += 50
            two += 50
        else :
            zero -= 50
            two -= 50
        time.sleep(0.5)
    time.sleep(0.5)
    # turn 1
    start=150
    for i in range(15) :
        pwm.set_pwm(1, 0, start)
        start += 30
        time.sleep(0.1)
    for i in range(15) :
        pwm.set_pwm(1, 0, start)
        start -= 30
        time.sleep(0.1)
    

    time.sleep(0.1)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(0, 0, 0)

    
def main() :
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(0, 0, 0)
    time.sleep(0.5)
    #test3()
    if n == str(87) : 
        dance()
        return
    else :
        # back to start point
        pwm.set_pwm(2, 0, 550)
        time.sleep(0.5)
        pwm.set_pwm(1, 0, 350)
        time.sleep(0.5)
        pwm.set_pwm(1, 0, 300)
        time.sleep(1)
        eval("cha_"+n+"()")
        time.sleep(1)
        # back to end
        pwm.set_pwm(2, 0, 560)
        pwm.set_pwm(0, 0, 180)
        time.sleep(3)
        pwm.set_pwm(1, 0, 250)
        time.sleep(0.1)
        pwm.set_pwm(1, 0, 300)
        time.sleep(0.1)
        pwm.set_pwm(1, 0, 350)
    time.sleep(0.1)
    pwm.set_pwm(2, 0, 0)
    pwm.set_pwm(1, 0, 0)
    pwm.set_pwm(0, 0, 0)
    return

main()
