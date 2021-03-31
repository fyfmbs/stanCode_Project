"""
File: hailstone.py
Name: Shawn Chan
-----------------------
This program should implement a console program that simulates
the execution of the Hailstone sequence, defined by Douglas
Hofstadter. Output format should match what is shown in the sample
run in the Assignment 2 Handout.
"""


def main():
    """
    This calculator would help user to list the Hailstone Sequence of the number they choose.
    """
    a = int(input('Type a positive integer:  '))
    # The variable "steps" used to count how many steps to reach 1.
    steps = 0
    while a != 1:
        if a % 2 == 0:
            b = a
            a //= 2
            steps += 1
            print(str(b) + ' is even, so I take half: ' + str(a))
        else:
            b = a
            a = a*3 + 1
            steps += 1
            print(str(b) + ' is odd, so I make 3n+1: ' + str(a))
    print('It took ' + str(steps) + ' steps to reach 1.')





###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
    main()
