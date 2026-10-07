# Practical 1
# Variables, Data Types and Operators
#Write Python programs to demonstrate variables, data types (int, float, str, bool) and all operators (Arithmetic, Assignment, 
Comparison, Logical, Membership, Identity, Bitwise).

name = "Greeva"
age = 20
height = 5.4
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)


a = 10
b = 3

print("\nArithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


x = 10
x += 5
print("\nAssignment Operator:", x)


print("\nComparison Operators")
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)


print("\nLogical Operators")
print(a > 5 and b < 5)
print(a > 5 or b > 5)
print(not(a > 5))


numbers = [1, 2, 3, 4, 5]

print("\nMembership Operators")
print(3 in numbers)
print(10 not in numbers)


c = a
print("\nIdentity Operators")
print(a is c)
print(a is not b)


print("\nBitwise Operators")
print("AND:", a & b)
print("OR:", a | b)
print("XOR:", a ^ b)
print("NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)
