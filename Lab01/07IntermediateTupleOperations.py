# Tuple initialization
coordinates = (3, 5)

# Unpacking tuples
x, y = coordinates
print("x-coordinates:", x)  # Output: 3
print("y-coordinates:", y)  # Output: 5

# Tuple askeys indictionary
location = {(3, 5): "Home", (10, 20): "Office"}
print("location at (3,5):", location[(3, 5)])  # Output: Home
