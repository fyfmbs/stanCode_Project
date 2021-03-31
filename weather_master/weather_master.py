"""
File: weather_master.py
Name: Shawn Chan
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

EXIT = 100
# This constant controls when to stop.


def main():
	"""
	This program would help user to find out the critical weather conditions of the data,
	including the highest, the lowest and the average temperature,
	also the number of the cold days.
	"""
	print('stanCode "Weather Master 4.0"!')
	temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
	# The variable "count_input" used to count how many numbers we input.
	count_input = 1
	# The variable "cold_days" used to count how many days are lower than 16 degree Celsius.
	cold_days = 0
	if temp == EXIT:
		print('No temperatures were entered!!')
	else:
		maximum = temp
		minimum = temp
		total = temp
		if temp < 16:
			cold_days += 1
		while True:
			temp = int(input('Next Temperature: (or ' + str(EXIT) + ' to quit)? '))
			if temp == EXIT:
				average = total / count_input
				print('Highest Temperature = ' + str(maximum))
				print('Lowest Temperature = ' + str(minimum))
				print('Average = ' + str(average))
				print(str(cold_days) + ' Cold Day(s)')
				break
			if temp < 16:
				cold_days += 1
			if temp > maximum:
				maximum = temp
			elif temp < minimum:
				minimum = temp
			total = total + temp
			count_input += 1


###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
