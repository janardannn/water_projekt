import subprocess 
import random
import time
import sys
import select
import multiprocessing
from time_and_date import *
from playsound import playsound

class drink_water():

	def __init__(self):

		# how much glasses of water in a day? well it turns out that 15 is a 
		# very good number hence, daily water goal is set to 15 
		self.daily_water_goal = 15  
		# time interval between successive glasses (45min to 90min)
		self.random_duration_inbetween = random.randint(2750,5450)
		# incase you missed, prompts you again within 15-30 mins
		self.random_missed_duration = random.randint(900,1800)
		# to keep record of when you drank water
		self.log_file = open(r'/home/ironman/MySCripts/projekts/water_projekt/water.log','a+')

	def soundtrack(self):
		playsound(r'/home/ironman/MySCripts/projekts/water_projekt/Sunflower.mp3')

	def call_for_action(self):
		sound_trigger = multiprocessing.Process(target=self.soundtrack)
		done = 0
		for k in range(1,self.daily_water_goal+1):
			if done <= self.daily_water_goal:
				# using notify-send subprocess in linux and macos to send notifications
				# make sure DND is turned off 
				subprocess.call(['notify-send','Drink More Water','less water less mental efficiency'])

				# using the playsound module to play a random sound
				# as notifications are missed most of the time
				# input prompt
				sound_trigger.start()
				print('Drank water?(y/n): (press enter)')

				# using sys, select module to take a user input with timeout
				i, o, e = select.select( [sys.stdin], [], [], 330 )
				
				# if there is any input from user
				if (i):
					response = sys.stdin.readline().strip()
					if response == 'y' or response == 'Y':
						done += 1
						self.log_file.write('drank water at {}  --  {}\n'.format(time_now(),today_date()))
						print(f'{int(self.daily_water_goal-done)} more to gooo!')
						sound_trigger.terminate()
						print("-------------------------###----------------------------")
						time.sleep(self.random_duration_inbetween)

					elif response == 'n' or response == 'N':
						print('Make sure you drink next time!')
						sound_trigger.terminate()
						print("-------------------------###----------------------------")
						time.sleep(self.random_missed_duration)
				# else just cotinue	
				else:
					print('No response!')
					print('Make sure you drink next time!')
					sound_trigger.terminate()
					print("-------------------------###----------------------------")
					time.sleep(self.random_missed_duration)

			else:
				self.log_file.close()
					
				

drink_water_healthy_life = drink_water()
drink_water_healthy_life.call_for_action()
