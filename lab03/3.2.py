def generate_patterns(n, current=0, results=None):
    results1 = ""
    results2 = ""
    results3 = ""
    results4 = ""
    results5 = ""

    if current == n:
        return results1, results2, results3, results4, results5

    line1 = "*" * (current + 1)
    line2 = " " * (n - current - 1) + "*" * (current + 1)
    line3 = "*" * (n - current)
    line4 = " " * (n - current - 1) + "* " * (current + 1)
    line5 = " " * current + "* " * (n - current)

    results1 += line1 + "\n"
    results2 += line2 + "\n"
    results3 += line3 + "\n"
    results4 += line4 + "\n"
    results5 += line5 + "\n"

    return generate_patterns(n, current + 1, results)


def generateline(n):
    print("-" * n)


x = int(input("Enter a number (integer): "))

pattern1, pattern2, pattern3, pattern4, pattern5 = generate_patterns(x)

print(pattern1)
generateline(x * 2)
print(pattern2)
generateline(x * 2)
print(pattern3)
generateline(x * 2)
print(pattern4)
generateline(x * 2)
print(pattern5)
