# Practical 7
# MySQL CRUD Operations
#Connect Python with MySQL database and perform Create, Read,
Update and Delete (CRUD) operations.
  

import mysql.connector


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=" ",
    database="pds"
)

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    marks INT
)
""")


cursor.execute(
    "INSERT INTO students VALUES (1, 'Greeva', 85)"
)

connection.commit()


cursor.execute("SELECT * FROM students")

print("Student Records:")

for row in cursor.fetchall():
    print(row)


cursor.execute(
    "UPDATE students SET marks = 90 WHERE id = 1"
)

connection.commit()


cursor.execute(
    "DELETE FROM students WHERE id = 1"
)

connection.commit()

print("CRUD operations completed.")

cursor.close()
connection.close()
