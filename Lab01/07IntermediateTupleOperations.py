# Tuple initialization
coordinates = (3, 5)  # สร้าง tuple แต่ไม่สามารถเปลี่ยนค่าได้

# Unpacking tuples
x, y = coordinates  # กำหนดตัวแปรเพื่อเรียกใช้ tuple แต่ละตัว
print("x-coordinates:", x)  # Output: 3
print("y-coordinates:", y)  # Output: 5

# Tuple askeys indictionary
location = {(3, 5): "Home", (10, 20): "Office"}  # สร้าง tuple โดยกำหนดค่า Directory มาด้วย
print("location at (3,5):", location[(3, 5)])  # Output: Home
