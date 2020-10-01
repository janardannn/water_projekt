import subprocess 
import random
import time
import sys
import select
import multiprocessing
from time_and_date import *
from playsound import playsound
from configparser import ConfigParser

class drink_water():

	def __init__(self,path_to_logfile,path_to_soundtrack):

		# how much glasses of water in a day? well it turns out that 15 is a 
		# very good number hence, daily water goal is set to 15 
		self.daily_water_goal = 15  
		# time interval between successive glasses (45min to 90min)
		self.random_duration_inbetween = random.randint(2750,5450)
		# incase you missed, prompts you again within 15-30 mins
		self.random_missed_duration = random.randint(900,1800)
		# to keep record of when you drank water
		self.log_file = open(path_to_logfile,'a+')

	def soundtrack(self):
		# using the playsound module to play a random sound
		# as notifications are missed most of the time
		while True:
			playsound(path_to_soundtrack)

	def spam_notifications(self):
		# using notify-send subprocess in linux and macos to send notifications
		# make sure DND is turned off
		while True:
			subprocess.call(['notify-send','Drink More Water','less water less mental efficiency'])
		# sleep time between succesive notification(s)
			time.sleep(5)

	def call_for_action(self):
		sound_trigger = multiprocessing.Process(target=self.soundtrack)
		notification_trigger = multiprocessing.Process(target=self.spam_notifications)
		done = 0
		for k in range(1,self.daily_water_goal+1):
			if done <= self.daily_water_goal:
				# input prompt
				sound_trigger.start()
				notification_trigger.start()
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

						notification_trigger.terminate()
						sound_trigger.terminate()

						print("-------------------------###----------------------------")
						time.sleep(self.random_duration_inbetween)

					elif response == 'n' or response == 'N':
						print('Make sure you drink next time!')

						notification_trigger.terminate()
						sound_trigger.terminate()

						print("-------------------------###----------------------------")
						time.sleep(self.random_missed_duration)

					elif response == "" or response == " ":
						done += 1
						self.log_file.write('drank water at {}  --  {}\n'.format(time_now(),today_date()))
						print(f'{int(self.daily_water_goal-done)} more to gooo!')

						notification_trigger.terminate()
						sound_trigger.terminate()

						print("-------------------------###----------------------------")
						time.sleep(self.random_duration_inbetween)

				# else just cotinue	
				else:
					print('No response!')
					print('Make sure you drink next time!')

					notification_trigger.terminate()
					sound_trigger.terminate()

					print("-------------------------###----------------------------")
					time.sleep(self.random_missed_duration)

			else:
				self.log_file.close()
					
				
###### reading config.ini for paths
parser = ConfigParser()
parser.read('config.ini')
path_to_logfile = parser.get('paths','logfile')
path_to_soundtrack = parser.get('paths','soundtrack')

drink_water_healthy_life = drink_water(path_to_logfile,path_to_soundtrack)
drink_water_healthy_life.call_for_action()
