def generate_patterns(
    n, current=1, results1="", results2="", results3="", results4="", results5=""
):
    if current > n:
        return results1, results2, results3, results4, results5

    line1 = "*" * current
    line2 = " " * (n - current) + "*" * current
    line3 = "*" * (n - current + 1)
    line4 = " " * (n - current) + "* " * current
    line5 = " " * (current - 1) + "* " * (n - current + 1)

    results1 += line1 + "\n"
    results2 += line2 + "\n"
    results3 += line3 + "\n"
    results4 += line4 + "\n"
    results5 += line5 + "\n"

    return generate_patterns(
        n, current + 1, results1, results2, results3, results4, results5
    )


def generateline(n):
    print("-" * (n * 2))


x = int(input("Enter a number (integer): "))

pattern1, pattern2, pattern3, pattern4, pattern5 = generate_patterns(x)

print(pattern1)
generateline(x)
print(pattern2)
generateline(x)
print(pattern3)
generateline(x)
print(pattern4)
generateline(x)
print(pattern5)
