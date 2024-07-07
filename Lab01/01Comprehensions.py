# List Comprehension
# x^2 0->9 times
squares = [x**2 for x in range(10)]

# Dictionary Comprehension
# make a varailble x and x^2 0->4
square_dict = {x: x**2 for x in range(5)}

# Set comprehension
# print a even number
even_squares = {x**2 for x in range(10) if x % 2 == 0}

print(squares)
print(square_dict)
print(even_squares)
