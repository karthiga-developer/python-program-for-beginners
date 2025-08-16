"""
Program Name : count_suppliers.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Counts the number of book suppliers entered by the user.
"""

def count_book_suppliers():
    suppliers = []
    print("Enter the names of book suppliers (type 'done' to finish):")
    while True:
        name = input("Supplier name: ")
        if name.lower() == 'done':
            break
        suppliers.append(name)
    print(f"\nTotal number of book suppliers: {len(suppliers)}")

if __name__ == "__main__":
    count_book_suppliers()