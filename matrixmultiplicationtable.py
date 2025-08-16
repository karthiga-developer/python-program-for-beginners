"""
Program Name : matrixmultiplicationtable.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Displays the multiplication table for a matrix or a given number.
"""

rows = 10
cols = 10

print("Matrix Multiplication Table:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
          print(f"{i*j:4}", end=" ")
    print()