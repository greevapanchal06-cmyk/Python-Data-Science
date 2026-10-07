# Practical 2
# List, Tuple, Set, Dictionary and String
#Demonstrate creation and manipulation of list, tuple, set, dictionary
and string with their built-in methods.

numbers = [10, 20, 30, 40]

print("List:", numbers)

numbers.append(50)
numbers.remove(20)
numbers.sort()

print("After manipulation:", numbers)
print("Length:", len(numbers))


fruits = ("Apple", "Banana", "Mango")

print("\nTuple:", fruits)
print("First fruit:", fruits[0])
print("Number of fruits:", len(fruits))


colors = {"Red", "Blue", "Green"}

print("\nSet:", colors)

colors.add("Yellow")
colors.remove("Blue")

print("After manipulation:", colors)


student = {
    "name": "Greeva",
    "age": 20,
    "course": "Computer Engineering"
}

print("\nDictionary:", student)
print("Name:", student["name"])

student["age"] = 21
student["city"] = "Surat"

print("Updated Dictionary:", student)


text = "Python for Data Science"

print("\nString:", text)
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Length:", len(text))
print("Replace:", text.replace("Python", "PDS"))
print("Split:", text.split())
