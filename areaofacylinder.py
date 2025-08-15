"""
areaofacylinder.py

This script calculates the curved surface area (CSA) of a cylinder using user-provided radius and height.
Formula used:
    CSA = 2 * π * r * h
Where:
    r = radius of the cylinder
    h = height of the cylinder

Author: Karthiga
Date: August 15, 2025
"""

import math

def curved_surface_area_cylinder(radius, height):
    """
    Calculate the curved surface area (CSA) of a cylinder.
    CSA = 2 * π * r * h

    Args:
        radius (float): Radius of the cylinder.
        height (float): Height of the cylinder.

    Returns:
        float: Curved surface area of the cylinder.
    """
    return 2 * math.pi * radius * height

# Example usage:
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
csa = curved_surface_area_cylinder(r, h)
print(f"Curved Surface Area of the cylinder: {csa:.3f}")