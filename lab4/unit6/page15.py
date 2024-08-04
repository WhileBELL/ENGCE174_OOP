# Example 4: Set operations and methods

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Adding elements to a set
set1.add(5)

# Removing elements from a set
set2.discard(6)

# Checking subset and superset
print(
    "Is set1 a subset of set2?", set1.issubset(set2)
)  # Output: Is set1 a subset of set2? False
print(
    "Is set2 a subset of set1?", set2.issubset(set1)
)  # Output: Is set2 a subset of set1? True
