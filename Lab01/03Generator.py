def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci()
print(next(fib))  # Output:0
print(next(fib))  # OUtput:1
