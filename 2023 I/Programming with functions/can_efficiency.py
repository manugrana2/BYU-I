"""This script calculates the storage efficiency of a list of different can types."""
import math

def main():

    def  volume(radius, height):
        x = math.pi * radius ** 2 * height 
        return x
    
    def surface_area (radius, height):
        x = math.pi * 2 * radius * (radius + height)
        return x
    
    def storage_efficiency(volume, surface_area):
        x = volume / surface_area
        return x

    name = ""
    efficiency = 0

    names = ["#1 Picnic", "#1 Tall", "#2", "#2.5", "#3 Cylinder", "#5", "#6Z", "#8Z short", "#10", "#211", "#300", "#303"]
    radius_list = [6.83, 7.78, 8.73, 10.32, 10.79, 13.02, 5.40, 6.83, 15.72, 6.83, 7.62, 8.10]
    height_list = [10.16, 11.91, 11.59, 11.91, 17.78, 14.29, 8.89, 7.62, 17.78, 12.38, 11.27, 11.11]
    for i in range(len(radius_list)):
      radius = radius_list[i]
      print(radius)
      height = height_list[i]
      can_volume = volume(radius, height)
      can_surface_area = surface_area(radius, height)
      final_answer = storage_efficiency(can_volume, can_surface_area)
      print(f'The storage efficiency of {names[i]} is {final_answer:.2f}.')

      if i == 0:
        efficiency = final_answer
      elif final_answer > efficiency:
        name = names[i]
        

    print(f'\n The can with the highest storage efficiency is {name} with {efficiency:.2f} efficiency.')

main()