#Practical 11
#Use Pandas to create Series and DataFrames, perform data selection,filtering, grouping and aggregation operations.

import pandas as pd


marks = pd.Series([85, 90, 78, 92, 88])

print("Series:")
print(marks)


data = {
    "Name": ["Amit", "Rahul", "Neha", "Priya", "Jay"],
    "Department": ["CSE", "IT", "CSE", "IT", "CSE"],
    "Marks": [85, 90, 78, 92, 88],
    "Age": [20, 21, 20, 22, 21]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


print("\nSelect Marks column:")
print(df["Marks"])

print("\nSelect first three rows:")
print(df.iloc[:3])


print("\nStudents with Marks > 85:")
print(df[df["Marks"] > 85])

print("\nCSE Students:")
print(df[df["Department"] == "CSE"])


print("\nGroup by Department:")
print(df.groupby("Department")["Marks"].mean())


print("\nAggregation:")
print("Total Marks =", df["Marks"].sum())
print("Average Marks =", df["Marks"].mean())
print("Maximum Marks =", df["Marks"].max())
print("Minimum Marks =", df["Marks"].min())

print("\nDepartment-wise Aggregation:")
print(df.groupby("Department")["Marks"].agg(["mean", "max", "min", "count"]))
