# List comprehension to create ae lift of squares of even numbers
even_numbers = [x for x in range(10) if x % 2 == 0]
squares = [num**2 for num in even_numbers]
print("Squares of even numbers:", squares)  # Output:[0,4,16,36,64]
