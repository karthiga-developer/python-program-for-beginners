"""
Program Name : calculate_electric_bill.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Calculates the total electric bill based on units consumed and rate per unit.
"""

def calculate_electric_bill():
    try:
        units = float(input("Enter the number of units consumed: "))
        rate = float(input("Enter the rate per unit: "))
        bill = units * rate
        print(f"\nYour total electric bill is: ₹{bill:.2f}")
    except ValueError:
        print("Please enter valid numbers for units and rate.")

if __name__ == "__main__":
    calculate_electric_bill()