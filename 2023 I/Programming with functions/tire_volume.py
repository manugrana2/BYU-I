import math
from datetime import datetime
"""Python program that reads from the keyboard the three numbers for a tire 
and computes and outputs the volume of space inside that tire.
"""
#Get the current time
current_date_and_time = datetime.now()
#Get the tire with from user
width = float(input("Enter the width of the tire in mm (e.g 205): "))
#Get the tire aspect ratio from user
aspect_ratio = float(input("Enter the aspect ratio of the tire (e.g 60): "))
#Get the diameter with from user
diameter = float(input("Enter the diameter of the wheel in inches (e.g 15): "))
#Calculate the tire volume using the formula
tire_volume = (math.pi*(width**2)*aspect_ratio*(width * aspect_ratio + 2540 * diameter))/10000000000
#Write the tire meassures info and date to a file
print(f"The approximate volume is {round(tire_volume, 2)} liters")
tire_price = 0


with open("volumes.txt", "at") as cities_file:
    print(f"{current_date_and_time:%Y-%m-%d}, {int(width)}, {int(aspect_ratio)}, {int(diameter)}, {round(tire_volume,2)}", file=cities_file)

