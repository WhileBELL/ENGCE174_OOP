def fibonacci():  # กำหนด function fib
    a, b = 0, 1
    while True:
        yield a  # เป็นคำสั่งที่ใช้คืนค่าตัวที่กำหนดออกไปจาก func ก่อนที่ variable จะถูกเปลี่ยนแปลง แต่ก็จะถูกอัพเดทอยู่ดี
        a, b = b, a + b


fib = fibonacci()
print(next(fib))  # Output:0
print(next(fib))  # Output:1
