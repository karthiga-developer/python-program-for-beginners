"""
Program Name : days_between.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Calculates the number of days between two dates.
"""

from datetime import datetime

# Input format: YYYY-MM-DD
date_str1 = input("Enter the second date (YYYY-MM-DD): ")
date_str2 = input("Enter the second date (YYYY-MM-DD): ")

date1 = datetime.strptime(date_str1, "%Y-%m-%d")
date2 = datetime.strptime(date_str2, "%Y-%m-%d")

days_between = abs((date2 - date1).days)
print(f"Number of days between {date_str1} and {date_str2}: {days_between}")