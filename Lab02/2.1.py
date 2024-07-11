# รับค่าความสูงผ่านทาง keyboard
height = int(input("Enter height (integer): "))

# พิมพ์ลำดับดาวที่ 1
for i in range(1, height + 1):
    print("*" * i)
print("-------------")

# พิมพ์ลำดับดาวที่ 2
for n in range(height, 0, -1):
    print("*" * n)
print("-------------")

# พิมพ์ลำดับดาวที่ 3
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end=" ")
    print()

print("-------------")

# พิมพ์ลำดับดาวที่ 4
for i in range(height, 0, -1):
    for j in range(height - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    print()

print("-------------")

# พิมพ์ลำดับดาวที่ 5
for i in range(height):
    for j in range(height - i - 1):
        print(" ", end="")
    for k in range(i + 1):
        print("*", end="")
    print()
