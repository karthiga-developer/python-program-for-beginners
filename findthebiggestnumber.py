"""
Program Name : findthebiggestnumber.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Takes three numbers from the user and prints the biggest one without using the max() function.
"""

# Input: three numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

# Find the biggest number without using max()
if num1 >= num2 and num1 >= num3:
    biggest = num1
elif num2 >= num1 and num2 >= num3:
    biggest = num2
else:
    biggest = num3

# Output the result
print("The biggest number is:", biggest)