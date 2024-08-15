def generate_patterns(height):
    results1 = ""
    results2 = ""
    results3 = ""
    results4 = ""
    results5 = ""
    line = "-" * height * 2

    # Pattern 1
    for i in range(1, height + 1):
        results1 += "*" * i + "\n"

    # Pattern 2
    for n in range(height, 0, -1):
        results2 += "*" * n + "\n"

    # Pattern 3
    for i in range(height):
        for j in range(height - i - 1):
            results3 += " "
        for k in range(i + 1):
            results3 += "* "
        results3 += "\n"

    # Pattern 4
    for i in range(height, 0, -1):
        for j in range(height - i):
            results4 += " "
        for k in range(i):
            results4 += "* "
        results4 += "\n"

    # Pattern 5
    for i in range(height):
        for j in range(height - i - 1):
            results5 += " "
        for k in range(i + 1):
            results5 += "*"
        results5 += "\n"

    return results1, results2, results3, results4, results5, line


height = int(input("Enter height (integer): "))

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
