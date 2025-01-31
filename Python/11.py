import math

# Input: radius and height of the cylinder
radius = int(input("Enter the radius of the cylinder: "))
height = int(input("Enter the height of the cylinder: "))

# Calculate surface area
# Surface Area = 2 * π * radius * (radius + height)
surface_area = 2 * math.pi * radius * (radius + height)

# Calculate volume
# Volume = π * radius^2 * height
volume = math.pi * radius ** 2 * height

# Output the results
print(f"Surface Area of the cylinder: {surface_area:.2f}")
print(f"{volume:.2f}")