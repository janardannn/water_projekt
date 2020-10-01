import subprocess 
import random
import time
import sys
import select
from time_and_date import *
##
class drink_water():

	def __init__(self):
		self.daily_water_goal = 15 
		self.random_duration_inbetween = random.randint(2750,5450)
		self.log_file = open(r'/home/ironman/MySCripts/projekts/water_projekt/water.log','a+')

	def call_for_action(self):
		done = 0
		for k in range(1,self.daily_water_goal+1):
			if done <= self.daily_water_goal:
				subprocess.call(['notify-send','Drink More Water','less water less mental efficiency'])
				print('Drank water?(y/n): (press enter)')
				i, o, e = select.select( [sys.stdin], [], [], 330 )
				
				if (i):
					response = sys.stdin.readline().strip()
					if response == 'y' or response == 'Y':
						done += 1
						self.log_file.write('drank water at {}  --  {}\n'.format(time_now(),today_date()))
						print(f'{int(self.daily_water_goal-done)} more to gooo!')
						time.sleep(self.random_duration_inbetween)

					elif response == 'n' or response == 'N':
						print('Make sure you drink next time!')
						time.sleep(self.random_duration_inbetween)
					
				else:
					print('No response!')
					print('Make sure you drink next time!')
					time.sleep(self.random_duration_inbetween)
					print("-------------------------###----------------------------")
					continue
				

drink_water_healthy_life = drink_water()
drink_water_healthy_life.call_for_action()