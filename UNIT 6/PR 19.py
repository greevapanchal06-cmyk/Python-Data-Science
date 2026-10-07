#Practical 19
#Apply data preprocessing techniques: slicing, filtering, sorting,concatenating, aggregating and normalizing data using Pandas.


import pandas as pd

data1 = pd.DataFrame({
    "Name": ["Greeva", "Krisha"],
    "Marks": [80, 90]
})

data2 = pd.DataFrame({
    "Name": ["Yashvi", "Zeel"],
    "Marks": [85, 75]
})


print("Slicing:")
print(data1.iloc[0:2])



print("\nFiltering:")
print(data1[data1["Marks"] > 80])



data = pd.concat([data1, data2])

print("\nSorted Data:")
print(data.sort_values("Marks", ascending=False))



print("\nConcatenated Data:")
print(data)



print("\nAggregation:")
print("Average Marks:", data["Marks"].mean())


data["Normalized_Marks"] = (
    (data["Marks"] - data["Marks"].min()) /
    (data["Marks"].max() - data["Marks"].min())
)

print("\nNormalized Data:")
print(data)
