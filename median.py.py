"""
@author: Vishwa R
@License: MIT
@Date: 26-09-2022
@Version: v1.0.0
@Description: Generate color palette from an image using median cut
"""

# Built-in/Generic Imports
import sys

# Libs
from PIL import Image

# color range dominance detection
def findDominantColor(rgb_list):
    INT_MAX = sys.maxsize
    INT_MIN = -sys.maxsize - 1
    RED = 0
    GREEN = 1
    BLUE = 2

    rMin = INT_MAX
    gMin = INT_MAX
    bMin = INT_MAX

    rMax = INT_MIN
    gMax = INT_MIN
    bMax = INT_MIN

    for i in rgb_list:
        rMin = min(rMin, i[0])
        gMin = min(gMin, i[1])
        bMin = min(bMin, i[2])

        rMax = max(rMax, i[0])
        gMax = max(gMax, i[1])
        bMax = max(bMax, i[2])

    Range_r = rMax - rMin
    Range_g = gMax - gMin
    Range_b = bMax - bMin

    DominantRange = max(Range_r, Range_b, Range_g)

    if (DominantRange == Range_r):
        return RED
    elif DominantRange == Range_g:
        return GREEN
    else:
        return BLUE


# quantization of the rgb color space
def quantization(rgb_list, depth):
    MAX_DEPTH = 4
    RGB_LEN = len(rgb_list)

    if depth == MAX_DEPTH or RGB_LEN == 0:
        red_sum = 0
        green_sum = 0
        blue_sum = 0

        for i in rgb_list:
            red_sum += i[0]
            green_sum += i[1]
            blue_sum += i[2]

        colors = [red_sum, green_sum, blue_sum]

        colors[0] = round(colors[0] / RGB_LEN)
        colors[1] = round(colors[1] / RGB_LEN)
        colors[2] = round(colors[2] / RGB_LEN)

        return [colors]

    componentToSortBy = findDominantColor(rgb_list)

    rgb_list.sort(key = lambda rgb_list: rgb_list[componentToSortBy])

    mid = RGB_LEN // 2

    result = quantization(rgb_list[:mid], depth+1) + quantization(rgb_list[mid:], depth+1)

    return result

# RGB space to hex codes
def RGBtoHEX(pallete):
    # pallete => list[list]
    hex_pallete = []

    for i in pallete:
        hex_val = f'#{i[0]:02x}{i[1]:02x}{i[2]:02x}'
        hex_pallete.append(hex_val)
    return hex_pallete

arg_list = sys.argv
PATH = arg_list[1]

# open image for reading
img = Image.open(PATH, 'r')

# extracting pixel data
rgb_list = list(img.getdata())

quant_pallete = quantization(rgb_list, 0)
final_hex = RGBtoHEX(quant_pallete)
print("RGB PALLETE")
print(quant_pallete)
print()
print("HEX PALLETE")
print(final_hex)
