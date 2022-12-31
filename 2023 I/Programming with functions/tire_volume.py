import math
"""Python program that reads from the keyboard the three numbers for a tire 
and computes and outputs the volume of space inside that tire.
"""
width = float(input("Enter the width of the tire in mm (e.g 205): "))
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g 60): "))
diameter = float(input("Enter the diameter of the wheel in inches (e.g 15): "))
tire_volume = (math.pi*(width**2)*aspect_ratio*(width * aspect_ratio + 2540 * diameter))/10000000000
print(f"The approximate volume is {round(tire_volume, 2)} liters")