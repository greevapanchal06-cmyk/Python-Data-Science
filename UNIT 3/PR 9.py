#Practical 9
#Demonstrate the data science life cycle and perform Univariate,Bivariate and Multivariate analysis on a real-world dataset.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("employee.csv")

print("Dataset Shape:", df.shape)
print("\nFirst 5 Records:")
print(df.head())

# ---------------- UNIVARIATE ANALYSIS ----------------


print("\nAge Statistics:")
print(df["Age"].describe())

plt.figure(figsize=(7, 4))
plt.hist(df["Age"], bins=10)
plt.xlabel("Age")
plt.ylabel("Number of Employees")
plt.title("Distribution of Employee Age")
plt.show()


print("\nAttrition Count:")
print(df["Attrition"].value_counts())

# ---------------- BIVARIATE ANALYSIS ----------------


plt.figure(figsize=(7, 4))
sns.scatterplot(data=df, x="Age", y="MonthlyIncome")
plt.xlabel("Age")
plt.ylabel("Monthly Income")
plt.title("Age vs Monthly Income")
plt.show()


print("\nDepartment and Attrition:")
print(pd.crosstab(df["Department"], df["Attrition"]))

# ---------------- MULTIVARIATE ANALYSIS ----------------

# Select numerical variables
cols = [
    "Age",
    "MonthlyIncome",
    "TotalWorkingYears",
    "YearsAtCompany"
]


correlation = df[cols].corr()

print("\nCorrelation Matrix:")
print(correlation)

plt.figure(figsize=(7, 5))
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.show()
