#Practical 16
#Plot and analyze Normal and Exponential continuous probabilitydistributions and demonstrate the Central Limit Theorem.



import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, expon


x = np.linspace(-4, 4, 100)

normal_values = norm.pdf(x, 0, 1)

plt.plot(x, normal_values)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.title("Normal Distribution")
plt.show()



x = np.linspace(0, 5, 100)

exponential_values = expon.pdf(x)

plt.plot(x, exponential_values)
plt.xlabel("Value")
plt.ylabel("Probability")
plt.title("Exponential Distribution")
plt.show()



data = np.random.randint(1, 100, 10000)

sample_means = []

for i in range(1000):
    sample = np.random.choice(data, 30)
    sample_means.append(np.mean(sample))

plt.hist(sample_means, bins=30)
plt.xlabel("Sample Mean")
plt.ylabel("Frequency")
plt.title("Central Limit Theorem")
plt.show()
