import math


def pain_calc(height, width, coverage):
    area = height * width
    no_of_cans = math.ceil(area / coverage)
    print(f"You will need {no_of_cans} cans of paint.")


h = int(input("Enter the height in meters: "))
w = int(input("Enter the width in meters: "))
coverage = 7

pain_calc(width=w, height=h, coverage=coverage)
