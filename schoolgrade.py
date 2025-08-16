"""
Program Name : schoolgrade.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Assigns a grade based on the marks entered by the user.
"""

# Python program to find your grade using if-else statement

marks = float(input("Enter your marks (0-100): "))

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
elif marks >= 50:
    grade = "E"
else:
    grade = "F"

print(f"Your grade is: {grade}")