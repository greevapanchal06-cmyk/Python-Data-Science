# Practical 6
# Exception Handling
#Demonstrate exception handling using try, except, else, finally
blocks and raise statement with custom exceptions.

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b

except ValueError:
    print("Please enter numbers only.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    print("Result:", result)

finally:
    print("Program completed.")


#  exception using raise

try:
    age = int(input("\nEnter your age: "))

    if age < 18:
        raise Exception("Age must be 18 or above.")

    print("You are eligible.")

except Exception as e:
    print("Error:", e)
