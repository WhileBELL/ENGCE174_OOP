def generate_patterns(n, current=0, results=None):
    if results is None:
        results = [""] * 5  # Initialize results for 5 patterns

    if current == n:
        return results

    line1 = "*" * (current + 1)
    line2 = " " * (n - current - 1) + "*" * (current + 1)
    line3 = "*" * (n - current)
    line4 = " " * (n - current - 1) + "* " * (current + 1)
    line5 = " " * current + "* " * (n - current)

    results[0] += line1 + "\n"
    results[1] += line2 + "\n"
    results[2] += line3 + "\n"
    results[3] += line4 + "\n"
    results[4] += line5 + "\n"

    return generate_patterns(n, current + 1, results)


def generateline(n):
    print("-" * n)


x = int(input("Enter a number (integer): "))

patterns = generate_patterns(x)

pattern1 = patterns[0]
pattern2 = patterns[1]
pattern3 = patterns[2]
pattern4 = patterns[3]
pattern5 = patterns[4]

print(pattern1)
generateline(x * 2)
print(pattern2)
generateline(x * 2)
print(pattern3)
generateline(x * 2)
print(pattern4)
generateline(x * 2)
print(pattern5)
