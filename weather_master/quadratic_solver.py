"""
File: quadratic_solver.py
Name: Shawn Chan
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation:
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	This is a calculator to help user finding out the roots of the quadratic equation.
	"""
	print('stanCode Quadratic Solver!')
	a = float(input("What's the coefficient of x^2? "))
	b = float(input("What's the coefficient of x? "))
	c = float(input("What's the constant of the equation? "))
	discriminant = b*b - 4*a*c
	if discriminant == 0:
		# The variable "root" stands for the only root of the quadratic equation.
		root = -b/(2*a)
		print('One root: ' + str(root))
	elif discriminant > 0:
		# The variable "sq_rt" stands for the square root of discriminant.
		sq_rt = math.sqrt(discriminant)
		# The variables "root1" & "root2" stand for the two real roots of the quadratic equation.
		root1 = (-b + sq_rt) / (2*a)
		root2 = (-b - sq_rt) / (2*a)
		print('Two roots: ' + str(root1) + " ， " + str(root2))
	else:
		print('No real roots')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
