# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
from tkinter import ttk
from PIL import ImageTk, Image
import colorsys
import cv2
from colormath.color_objects import LabColor
from colormath.color_diff import delta_e_cie1976
from colormath.color_diff import delta_e_cie1994
from colormath.color_diff import delta_e_cie2000
from colormath.color_diff import delta_e_cmc
import numpy

# Fix an issue with a deprecated function in Numpy
def patch_asscalar(a):
    return a.item()

setattr(numpy, "asscalar", patch_asscalar)

# function to convert from RGB to LAB
# .. list = [r, g, b]
def rgb2lab(list):
    num = 0
    # created list RGB and initialized with 0
    RGB = [0, 0, 0]
    for value in list:
        value = float(value) / 255
        if value > 0.04045:
            value = ((value + 0.055) / 1.055) ** 2.4
        else:
            value = value / 12.92
        RGB[num] = value * 100
        num = num + 1
    XYZ = [0, 0, 0, ]
    # converted all the three R, G, B to X, Y, Z
    X = RGB[0] * 0.4124 + RGB[1] * 0.3576 + RGB[2] * 0.1805
    Y = RGB[0] * 0.2126 + RGB[1] * 0.7152 + RGB[2] * 0.0722
    Z = RGB[0] * 0.0193 + RGB[1] * 0.1192 + RGB[2] * 0.9505
    # rounded off the values upto 4 decimal digit
    XYZ[0] = round(X, 4)
    XYZ[1] = round(Y, 4)
    XYZ[2] = round(Z, 4)
    XYZ[0] = float(XYZ[0]) / 95.047  # ref_X =  95.047   Observer= 2°, Illuminant= D65
    XYZ[1] = float(XYZ[1]) / 100.0  # ref_Y = 100.000
    XYZ[2] = float(XYZ[2]) / 108.883  # ref_Z = 108.883
    num = 0
    for value in XYZ:
        if value > 0.008856:
            value = value ** (0.3333333333333333)
        else:
            value = (7.787 * value) + (16 / 116)
        XYZ[num] = value
        num = num + 1

    # formed Lab list and initialize with 0
    Lab = [0, 0, 0]
    # found L, A, and B
    L = (116 * XYZ[1]) - 16
    a = 500 * (XYZ[0] - XYZ[1])
    b = 200 * (XYZ[1] - XYZ[2])
    # rounded off to 4 decimal digit
    Lab[0] = round(L, 4)
    Lab[1] = round(a, 4)
    Lab[2] = round(b, 4)
    return Lab

# function to find the difference between two color
def diff_win(rgbColor1, rgbColor2):

    # color1
    color1 = LabColor(lab_l=list1[0], lab_a=list1[1], lab_b=list1[2])
    # color2
    color2 = LabColor(lab_l=list2[0], lab_a=list2[1], lab_b=list2[2])

    delta_e1 = delta_e_cie1976(color1, color2)
    # print(delta_e1)
    delta_e2 = delta_e_cie1994(color1, color2)
    # print(delta_e2)
    delta_e3 = delta_e_cie2000(color1, color2)
    # print(delta_e3)
    delta_e4 = delta_e_cmc(color1, color2)
    # print(delta_e4)
    mbox.showinfo("Color Difference", "Color Difference\n\n1.)  Delta E CIE1976  :  " + str(delta_e1) + "\n\n2.)  Delta E CIE1994  :  " + str(delta_e2) + "\n\n3.)  Delta E CIE2000  :  " + str(delta_e3) + "\n\n4.)  Delta E CMC  :  " + str(delta_e4))

# function run the code to calculate the Delta E2000
# rgbColor1, rgbColor2 = [r, g, b]
def calculat_deltaE_CIE2000(rgbColor1, rgbColor2):

    # first convert the two colors from RGB -> LAB
    # rgb2lab -> list[l, a, b]
    # labList[] -> labColor
    labList1 = rgb2lab(rgbColor1)
    labColor1 = LabColor(lab_l=labList1[0], lab_a=labList1[1], lab_b=labList1[2])

    labList2 = rgb2lab(rgbColor2)
    labColor2 = LabColor(lab_l=labList2[0], lab_a=labList2[1], lab_b=labList2[2])

    # return the calculated Delta E CIE2000 value
    return delta_e_cie2000(labColor1, labColor2)



# Main section of code
def main():

    # gather / create two lists - [r, g, b]
    # temporary variabless for testing
    tempColor1 = [0, 0, 0]
    tempColor2 = [0, 0, 0]

    # calculate the delta E using the two created RGB lists
    _DeltaE_CIE2000 = calculat_deltaE_CIE2000(tempColor1, tempColor2)

    print("Hello World!")

# Run at startup
if __name__ == "__main__":
    main()