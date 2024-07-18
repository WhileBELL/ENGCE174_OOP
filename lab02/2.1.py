height = int(input("Enter height (integer): "))

for i in range(1, height + 1):
    print("*" * i)

print("-" * height * 2)

for n in range(height, 0, -1):
    print("*" * n)

print("-" * height * 2)

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()

print("-" * height * 2)

for i in range(height, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

print("-" * height * 2)

for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
