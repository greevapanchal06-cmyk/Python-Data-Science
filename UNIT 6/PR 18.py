#Practical 18
#Perform data cleaning operations: detect and handle missing values,remove duplicate records, and treat outliers in a dataset.


import pandas as pd

data = {
    "Name": ["Greeva", "Krisha", "Yashvi", "Zeel", "Zeel"],
    "Age": [20, 21, None, 20, 20],
    "Marks": [85, 90, 200, 80, 80]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)



print("\nMissing Values:")
print(df.isnull().sum())



df["Age"] = df["Age"].fillna(df["Age"].mean())



df = df.drop_duplicates()



df.loc[df["Marks"] > 100, "Marks"] = df["Marks"].median()

print("\nCleaned Data:")
print(df)
