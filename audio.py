import os
import random
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

#Based off GPIO of input
m2 = 4
M2 = 17
m3 = 27
M3 = 22
P4 = 5
A4 = 6
P5 = 13
PLAY = 19

#GPIO Input Buttons
GPIO.setup(m2, GPIO.IN)
GPIO.setup(M2, GPIO.IN)
GPIO.setup(m3, GPIO.IN)
GPIO.setup(M3, GPIO.IN)
GPIO.setup(P4, GPIO.IN)
GPIO.setup(A4, GPIO.IN)
GPIO.setup(P5, GPIO.IN)
GPIO.setup(PLAY, GPIO.IN)

#loops until a button is pressed, sets input_ to interval
def getInput():
	while True:
		if (GPIO.input(m2) == False):
			global input_
			input_ = m2
			return
		elif (GPIO.input(M2) == False):
			global input_
			input_ = M2
			return
		elif (GPIO.input(m3) == False):
			global input_
			input_ = m3
			return
		elif (GPIO.input(M3) == False):
			global input_
			input_ = M3
			return
		elif (GPIO.input(P4) == False):
			global input_
			input_ = P4
			return
		elif (GPIO.input(A4) == False):
			global input_
			input_ = A4
			return
		elif (GPIO.input(P5) == False):
			global input_
			input_ = P5
			return

#main loop
while True:
	#wait for play button
	GPIO.wait_for_edge(PLAY, GPIO.BOTH)

	#generate a random interval
	interval = random.randint(0, 6)

	#match for interval case
	if interval == 0:
		os.system('mpg123 -q min2.mp3')
		print "Playing m2 interval"
		getInput()
		if input_ == m2:
		os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
		os.system('mpg123 -q min2incorrect.mp3')
		os.system('mpg123 -q jaws.mp3')
			print "Wrong, here's a song"

	elif interval == 1:
		os.system('mpg123 -q maj2.mp3')
		print "Playing M2 interval"
		getInput()
		if input_ == M2:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q maj2incorrect.mp3')
			os.system('mpg123 -q bday.mp3')

	elif interval == 2:
		os.system('mpg123 -q min3.mp3')
		print "Playing m3 interval"
		getInput()
		if input_ == m3:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q min3incorrect.mp3')
			os.system('mpg123 -q greensleeves.mp3')

	elif interval == 3:
		os.system('mpg123 -q maj3.mp3')
		print "Playing M3 interval"
		getInput()
		if input_ == M3:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q maj3incorrect.mp3')
			os.system('mpg123 -q kumbaya.mp3')

	elif interval == 4:
		os.system('mpg123 -q P4.mp3')
		print "Playing P4 interval"
		getInput()
		if input_ == P4:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q P4incorrect.mp3')
			os.system('mpg123 -q bride.mp3')

	elif interval == 5:
		os.system('mpg123 -q A4.mp3')
		print "Playing A4 interval"
		getInput()
		if input_ == A4:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q A4incorrect.mp3')
			os.system('mpg123 -q maria.mp3')

	elif interval == 6:
		os.system('mpg123 -q P5.mp3')
		print "Playing P5 interval"
		getInput()
		if input_ == P5:
			os.system('mpg123 -q correct.mp3')
			print "Correct!"
		else:
			print "Wrong, here's a song."
			os.system('mpg123 -q P5incorrect.mp3')
			os.system('mpg123 -q twinkle.mp3')

	sleep(0.1);
