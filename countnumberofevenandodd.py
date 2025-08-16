"""
Program Name : countnumberofevenandodd.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Counts the number of even and odd numbers in a given range or list.
"""

even_count = 0
odd_count = 0

print("Enter 10 numbers:")

for i in range(10):
    num = int(input(f"Number {i+1}: "))
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print(f"Even numbers: {even_count}")
print(f"Odd numbers: {odd_count}")