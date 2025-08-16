"""
Program Name : sumandaverageof5numbers.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Calculates the sum and average of five numbers entered by the user.
"""

count = 0
total = 0

while count < 5:
    num = float(input(f"Enter number {count + 1}: "))
    total += num
    count += 1

average = total / 5

print(f"Sum of 5 numbers is: {total}")
print(f"Average of 5 numbers is: {average}")