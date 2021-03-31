"""
File: stanCodoshop.py
Name: Shawn Chan
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

TODO:
"""
import math  # import math package for calculated the square root
import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input(param):
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    color_dis = math.sqrt((red - pixel.red)**2 + (green - pixel.green)**2 + (blue - pixel.blue)**2)
    return color_dis


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input(param):
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    pixels_red = 0
    pixels_blue = 0
    pixels_green = 0
    for pixel in pixels:
        pixels_red += pixel.red
        pixels_blue += pixel.blue
        pixels_green += pixel.green
    return [pixels_red // len(pixels), pixels_green // len(pixels), pixels_blue // len(pixels)]


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input(param):
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    shortest_dis = 0
    # Used the get_average() function to get the RGB averages
    avg = get_average(pixels)
    best_pixel = 0
    for i in range(len(pixels)):
        pixel = pixels[i]
        dis = get_pixel_dist(pixel, avg[0], avg[1], avg[2])
        if i == 0:
            best_pixel = pixel
            shortest_dis = dis
        elif dis < shortest_dis:
            shortest_dis = dis
            best_pixel = pixel
    return best_pixel


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input(param):
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Write code to populate image and create the 'ghost' effect
    for x in range(width):
        for y in range(height):
            # Created a empty list for a single point(x, y) on each image
            pixel_lst = []
            result_pixel = result.get_pixel(x, y)
            # The image loop in the most inside is for the same coordinate but different image.
            for img in images:
                pixel_lst.append(img.get_pixel(x, y))
            result_pixel.red = get_best_pixel(pixel_lst).red
            result_pixel.green = get_best_pixel(pixel_lst).green
            result_pixel.blue = get_best_pixel(pixel_lst).blue

    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input(param):
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input(param):
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
