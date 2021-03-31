"""
File: largest_digit.py
Name: Shawn Chan
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	:param n: the number we want to find out the largest digit
	:return: the largest digit from the input number
	"""
	largest_digit = 0
	return largest_digit_help(n, largest_digit)


def largest_digit_help(n, largest_digit):
	"""
	A helper function for the find_largest_digit(n)

	:param n: the number we want to find out the largest digit
	:param largest_digit: a variable which assigned 0 at the beginning to save the largest digit
	:return: the largest digit from the input number
	"""
	n = abs(n)
	# if n/10 == 0 means n is a single digit
	if n // 10 == 0:
		if n > largest_digit:
			largest_digit = n
			return largest_digit
		else:
			return largest_digit
	elif largest_digit < n % 10:
		largest_digit = n % 10
		n //= 10
		return largest_digit_help(n, largest_digit)
	else:
		n //= 10
		return largest_digit_help(n, largest_digit)


if __name__ == '__main__':
	main()
