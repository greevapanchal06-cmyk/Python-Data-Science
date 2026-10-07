# Practical 3
# Conditional Statements and Loops
#Implement programs using if, if-else, elif, while loop, for loop,
nested loops, and loop control statements (break, continue, pass).

number = int(input("Enter a number: "))


if number > 0:
    print("Number is positive")


if number % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")


if number > 0:
    print("Positive number")
elif number < 0:
    print("Negative number")
else:
    print("Zero")


print("\nWhile Loop")

i = 1

while i <= 5:
    print(i)
    i += 1


print("\nFor Loop")

for i in range(1, 6):
    print(i)


print("\nNested Loop")

for i in range(1, 4):
    for j in range(1, 4):
        print("*", end=" ")
    print()


print("\nBreak")

for i in range(1, 10):
    if i == 5:
        break
    print(i)


print("\nContinue")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)


print("\nPass")

for i in range(1, 6):
    if i == 3:
        pass
    print(i)
