"""
Program Name : asciivalue.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Displays the ASCII value of a given character.
"""

ascii_value = int(input("Enter an ASCII value (0-127): "))
if 0 <= ascii_value <= 127:
    print(f"The character for ASCII value {ascii_value} is '{chr(ascii_value)}'")
else:
     print("Please enter a value between 0 and 127.")