"""
Program Name : eligibletovote.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Checks if the user is eligible to vote based on age.
"""

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")