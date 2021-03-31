"""
File: sierpinski.py
Name: Shawn Chan
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	TODO:
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: the order of the image
	:param length: the length of the triangle
	:param upper_left_x: the x_coordinate of the start point
	:param upper_left_y: the y_coordinate of the start point
	"""
	if order == 0:
		pass
	else:
		# draw the 1st triangle
		draw_triangle(length, upper_left_x, upper_left_y)
		# draw the upper left triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		# draw the upper right triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		# draw the bottom triangle
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + length / 2 * 0.866)


def draw_triangle(width, cor_x, cor_y):
	"""
	:param width: the length of the triangle
	:param cor_x: the x_coordinate of the start point
	:param cor_y: the y_coordinate of the start point
	"""
	l_side = GLine(cor_x, cor_y, cor_x + 0.5 * width, cor_y + 0.866 * width)
	upper_side = GLine(cor_x, cor_y, cor_x + width, cor_y)
	r_side = GLine(cor_x + width, cor_y, cor_x + 0.5 * width, cor_y + 0.866 * width)
	l_side.color = 'tomato'
	upper_side.color = 'tomato'
	r_side.color = 'tomato'
	window.add(l_side)
	window.add(upper_side)
	window.add(r_side)



if __name__ == '__main__':
	main()