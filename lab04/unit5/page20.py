# Given a list of numbers, remove all occurrences of a specific number and calculate the sum of remaining numbers.

numbers = [1, 2, 3, 4, 5, 3, 6, 7, 3]
remove_num = 3

# if there is number 3 in the list, it will loop untill there is none.
while remove_num in numbers:
    numbers.remove(remove_num)

print("Numbers after removal:", numbers)
print("Sum of remaining numbers:", sum(numbers))