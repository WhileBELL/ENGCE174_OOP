person = {"name": "Alice", "age": 30}

# Using get() method to handle missing keys
city = person.get("city", "unknown ")
print("City:", city)  # Output: Unknown
