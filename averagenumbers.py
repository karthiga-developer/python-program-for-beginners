# Dynamic initialization: values are provided by the user at runtime

count = int(input("How many numbers do you want to average? "))

total = 0
for i in range(count):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total / count if count != 0 else 0

print(f"The average is: {average}")