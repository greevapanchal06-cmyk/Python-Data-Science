#Practical 15
#Compute and visualize Binomial and Poisson probabilitydistributions using SciPy and Matplotlib.



import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, poisson


n = 10
p = 0.5

x = np.arange(0, n + 1)

binomial_values = binom.pmf(x, n, p)

plt.bar(x, binomial_values)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.title("Binomial Distribution")
plt.show()



lam = 4

x = np.arange(0, 15)

poisson_values = poisson.pmf(x, lam)

plt.bar(x, poisson_values)
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.title("Poisson Distribution")
plt.show()
