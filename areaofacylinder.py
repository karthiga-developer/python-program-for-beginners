import math

def curved_surface_area_cylinder(radius, height):
    """
    Calculate the curved surface area (CSA) of a cylinder.
    CSA = 2 * π * r * h
    """
    return 2 * math.pi * radius * height

# Example usage:
r = float(input("Enter the radius of the cylinder: "))
h = float(input("Enter the height of the cylinder: "))
csa = curved_surface_area_cylinder(r, h)
print(f"Curved Surface Area of the cylinder: {csa:.3f}")