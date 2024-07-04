names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "Chicag"]

# Using zip() for parallel iteration
for name, age, city in zip(names, ages, city):
    print(f"{name} is {age} year old and lives in {city}")
