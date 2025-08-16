"""
Program Name : celsius_to_fahrenheit.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Converts Celsius temperature to Fahrenheit.
"""

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius}°C is equal to {fahrenheit}°F")