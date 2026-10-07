# Practical 5
# File Handling
#Perform read, write and append operations on text files, CSV files,
and binary files using Python.

import csv

# ---------------- TEXT FILE ----------------


file = open("student.txt", "w")
file.write("Name: Greeva\n")
file.write("Course: Computer Engineering\n")
file.close()


file = open("student.txt", "a")
file.write("Subject: Python for Data Science\n")
file.close()


file = open("student.txt", "r")
print("Text File:")
print(file.read())
file.close()


# ---------------- CSV FILE ----------------


with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])
    writer.writerow(["Greeva", 20, 85])
    writer.writerow(["Krisha", 20, 90])
    writer.writerow(["Yashvi", 21, 88])



print("CSV File:")

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    for row in reader:
        print(row)


# ---------------- BINARY FILE ----------------

data = b"Hello Python"


with open("data.bin", "wb") as file:
    file.write(data)


with open("data.bin", "rb") as file:
    result = file.read()

print("\nBinary File:")
print(result)
