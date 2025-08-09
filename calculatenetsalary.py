# Program to calculate net salary

def calculate_net_salary(gross_salary, tax_rate, deductions):
    """
    Calculate net salary after tax and deductions.

    Args:
        gross_salary (float): The total salary before deductions.
        tax_rate (float): Tax rate as a percentage (e.g., 10 for 10%).
        deductions (float): Other deductions (e.g., insurance, provident fund).

    Returns:
        float: Net salary.
    """
    tax_amount = gross_salary * (tax_rate / 100)
    net_salary = gross_salary - tax_amount - deductions
    return net_salary

if __name__ == "__main__":
    try:
        gross_salary = float(input("Enter gross salary: "))
        tax_rate = float(input("Enter tax rate (%): "))
        deductions = float(input("Enter other deductions: "))
        net_salary = calculate_net_salary(gross_salary, tax_rate, deductions)
        print(f"Net Salary: {net_salary:.2f}")
    except ValueError:
         print("Invalid input. Please enter numeric values.")