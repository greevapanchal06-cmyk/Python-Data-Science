# Practical 4
# User-defined Functions and Built-in Modules
#Write Python programs using user-defined functions with different argument types and demonstrate use of built-in modules (math,
random, statistics).

import math
import random
import statistics


def message():
    print("Welcome to Python for Data Science")

message()



def add(a, b):
    return a + b

print("\nAddition:", add(10, 20))



def greet(name="Student"):
    print("Hello", name)

greet()
greet("Greeva")



def student(name, age):
    print("Name:", name)
    print("Age:", age)

student(age=20, name="Greeva")



def total(*numbers):
    return sum(numbers)

print("\nTotal:", total(10, 20, 30, 40))



print("\nMath Module")
print("Square root:", math.sqrt(25))
print("Power:", math.pow(2, 3))
print("Ceiling:", math.ceil(4.3))



print("\nRandom Module")
print("Random number:", random.randint(1, 100))


data = [10, 20, 30, 40, 50]

print("\nStatistics Module")
print("Mean:", statistics.mean(data))
print("Median:", statistics.median(data))
