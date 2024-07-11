from collections import namedtuple

# Define a named tuple
Point = namedtuple("Point", ["x", "y"])  # สร้าง tuple โดยกำหนดค่า Directory ก่อน Key

# Create instances of the named tuple
p1 = Point(3, 5)  # กำหนดค่า Key
p2 = Point(-1, 2)  # กำหนดค่า Key

# Access elements by name
print("Coordinates of p1:", p1.x, p1.y)  # Output: 3 5
