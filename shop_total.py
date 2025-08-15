# shop_total.py

def calculate_total():
    total = 0
    num_items = int(input("Enter number of items: "))
    for i in range(num_items):
        price = float(input(f"Enter price of item {i+1}: "))
        quantity = int(input(f"Enter quantity of item {i+1}: "))
        total += price * quantity
    print(f"Total amount: ${total:.2f}")

if __name__ == "__main__":
    calculate_total()