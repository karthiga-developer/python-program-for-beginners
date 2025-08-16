"""
Program Name : evenoroddnumber.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Determines whether a given number is even or odd.
"""

# Program to check if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(f"{num} is an even number.")
else:
    print(f"{num} is an odd number.")