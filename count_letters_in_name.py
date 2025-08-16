"""
Program Name : count_letters_in_name.py
Author       : Karthiga
Date         : 2025-08-16
Purpose      : Counts the number of letters in a user's name.
"""

def count_letters(name):
    """
    Count the number of alphabetic letters in the given name.

    Args:
        name (str): The name to count letters in.

    Returns:
        int: Number of letters in the name.
    """
    return sum(1 for char in name if char.isalpha())

# Example usage:
user_name = input("Enter your name: ")
letter_count = count_letters(user_name)
print(f"Number of letters in your name: {letter_count}")