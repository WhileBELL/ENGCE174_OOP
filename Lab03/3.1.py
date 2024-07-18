def generate_patterns(height):
    pattern1 = ""
    pattern2 = ""
    pattern3 = ""
    pattern4 = ""
    pattern5 = ""
    line = "-" * height * 2

    # Pattern 1
    for i in range(1, height + 1):
        pattern1 += "*" * i + "\n"

    # Pattern 2
    for n in range(height, 0, -1):
        pattern2 += "*" * n + "\n"

    # Pattern 3
    for i in range(height):
        for j in range(height - i - 1):
            pattern3 += " "
        for k in range(i + 1):
            pattern3 += "* "
        pattern3 += "\n"

    # Pattern 4
    for i in range(height, 0, -1):
        for j in range(height - i):
            pattern4 += " "
        for k in range(i):
            pattern4 += "* "
        pattern4 += "\n"

    # Pattern 5
    for i in range(height):
        for j in range(height - i - 1):
            pattern5 += " "
        for k in range(i + 1):
            pattern5 += "*"
        pattern5 += "\n"

    return pattern1, pattern2, pattern3, pattern4, pattern5, line


# รับค่าความสูงจากผู้ใช้
height = int(input("Enter height (integer): "))

# เรียกใช้ฟังก์ชันเพื่อพิมพ์ patterns
pattern1, pattern2, pattern3, pattern4, pattern5, line = generate_patterns(height)

print(pattern1)
print(line)
print(pattern2)
print(line)
print(pattern3)
print(line)
print(pattern4)
print(line)
print(pattern5)
print(line)
