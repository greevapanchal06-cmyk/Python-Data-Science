#Practical 8
#Calculate and interpret descriptive statistics: mean, median, mode, variance, standard deviation, range, quartiles and IQR on a given
dataset.


import pandas as pd


df = pd.read_csv("employee.csv")


age = df["Age"]


mean = age.mean()
median = age.median()
mode = age.mode()[0]
variance = age.var()
std = age.std()
data_range = age.max() - age.min()

Q1 = age.quantile(0.25)
Q2 = age.quantile(0.50)
Q3 = age.quantile(0.75)
IQR = Q3 - Q1

print("Mean =", mean)
print("Median =", median)
print("Mode =", mode)
print("Variance =", variance)
print("Standard Deviation =", std)
print("Range =", data_range)
print("Q1 =", Q1)
print("Q2 =", Q2)
print("Q3 =", Q3)
print("IQR =", IQR)
