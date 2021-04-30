#import the GPIO package
import RPi.GPIO as GPIO
testPin = 23
#set pin 4 to input and the initial value to zero
GPIO.setmode(GPIO.BCM)
GPIO.setup(testPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



#set program to always be listening
print("Waiting for input on pin: " + str(testPin))
while 1==1:
    #check for the signal
    if GPIO.input(testPin) == GPIO.HIGH:
        #display "Signal Detected!" when the signal is received
        print("Signal Detected!")
