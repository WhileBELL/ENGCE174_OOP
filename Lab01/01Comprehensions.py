# List Comprehension
squares = [x**2 for x in range(10)]

# Dictionary Comprehension
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
even_squares = {x**2 for x in range(10) if x % 2 == 0}

print(squares)
print(square_dict)
print(even_squares)
