"""
Program Name : averagenumbers.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Asks the user how many numbers they want to average, takes those numbers as input, and prints the average.
"""

# Dynamic initialization: values are provided by the user at runtime

count = int(input("How many numbers do you want to average? "))

total = 0
for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / count if count != 0 else 0

print(f"The average is: {average}")