#Practical 17
#Perform hypothesis testing using one sample t-test and interpret results based on p-value and significance level.



from scipy.stats import ttest_1samp

marks = [72, 75, 68, 80, 74, 77, 70, 76, 73, 78]


population_mean = 70

t_statistic, p_value = ttest_1samp(
    marks,
    population_mean
)

print("T-statistic:", t_statistic)
print("P-value:", p_value)

alpha = 0.05

if p_value < alpha:
    print("Reject the null hypothesis.")
    print("There is a significant difference.")
else:
    print("Accept the null hypothesis.")
    print("There is no significant difference.")
