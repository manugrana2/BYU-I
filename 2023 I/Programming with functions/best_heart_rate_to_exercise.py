"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""
age = float(input("What is your age: "))
max_heart_rate = 200-age
range_from = max_heart_rate * 0.65
range_to = max_heart_rate * 0.85
print(f"When you exercise to strengthen your heart, you shouldkeep your heart rate between {range_from} and {range_to} beats per minute.")