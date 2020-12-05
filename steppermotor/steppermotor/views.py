from django.shortcuts import render
from django.http import HttpResponse
from time import sleep
import RPi.GPIO as GPIO

def home(request):
 	return render(request,'home.html')

def CLK(request):
	motor_channel = (29,31,33,35)
 	GPIO.setwarnings(False)
 	GPIO.setmode(GPIO.BOARD)
 	GPIO.setup(motor_channel, GPIO.OUT)
	motor_direction=1
 	for i in range (100):
 		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
 		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
 		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
 		sleep(0.02)
 	return(HttpResponse('Running motor in anticlockwise direction'))

def ANTCLK(request):
 	motor_channel = (29,31,33,35)
 	GPIO.setwarnings(False)
 	GPIO.setmode(GPIO.BOARD)
 	GPIO.setup(motor_channel, GPIO.OUT)
 	motor_direction=1
 	for i in range (100):
 		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.LOW,GPIO.LOW,GPIO.HIGH))
 		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.HIGH,GPIO.HIGH,GPIO.LOW,GPIO.LOW))
 		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.LOW,GPIO.HIGH,GPIO.HIGH,GPIO.LOW))
 		sleep(0.02)
 		GPIO.output(motor_channel, (GPIO.LOW,GPIO.LOW,GPIO.HIGH,GPIO.HIGH))
 		sleep(0.02)
 	return(HttpResponse('Running motor in clockwise direction'))