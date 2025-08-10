rows = 10
cols = 10

print("Matrix Multiplication Table:")
for i in range(1, rows + 1):
    for j in range(1, cols + 1):
          print(f"{i*j:4}", end=" ")
    print()