"""
Program Name : staff_present.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Counts the number of staff present based on user input.
"""

def count_staff_present():
    total_staff = int(input("Enter total number of staff: "))
    present_count = 0
    for i in range(total_staff):
        status = input(f"Is staff member {i+1} present? (yes/no): ").strip().lower()
        if status == "yes":
            present_count += 1
    print(f"Number of staff present: {present_count}")

if __name__ == "__main__":
    count_staff_present()