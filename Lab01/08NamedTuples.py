from collections import namedtuple

# Define a named tuple
Point = namedtuple("Point", ["x", "y"])

# Create instances of the named tuple
p1 = Point(3, 5)
p2 = Point(-1, 2)

# Access elements by name
print("Coordinates of p1:", p1.x, p1.y)  # Output: 3 5
