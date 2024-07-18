names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
city = ["New York", "Los Angeles", "Chicag"]

# Using zip() for parallel iteration
for name, age, city in zip(
    names, ages, city
):  # zip ใช้ในการเข้าถึง variable ใน list ทุกตัวและทุก list แบบพร้อมๆ กัน
    print(f"{name} is {age} year old and lives in {city}")
