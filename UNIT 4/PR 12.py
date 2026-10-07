#Practical 12
#Use SciPy's stats module to compute statistical measures andperform statistical tests on datasets.

import numpy as np
from scipy import stats


data = np.array([10, 12, 15, 15, 18, 20, 22, 25, 30])


print("Dataset:", data)
print("Mean:", stats.tmean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data).mode)
print("Variance:", stats.tvar(data))
print("Standard Deviation:", stats.tstd(data))
print("Skewness:", stats.skew(data))
print("Kurtosis:", stats.kurtosis(data))


t_test = stats.ttest_1samp(data, 18)

print("\nOne Sample T-Test")
print("T-statistic:", t_test[0])
print("P-value:", t_test[1])


shapiro_test = stats.shapiro(data)

print("\nShapiro-Wilk Test")
print("Statistic:", shapiro_test[0])
print("P-value:", shapiro_test[1])


x = [10, 20, 30, 40, 50]
y = [12, 25, 28, 42, 55]

correlation = stats.pearsonr(x, y)

print("\nPearson Correlation Test")
print("Correlation:", correlation[0])
print("P-value:", correlation[1])
