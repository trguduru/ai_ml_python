# guassian distribution
from scipy.stats import uniform
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

gauss1 = norm(5, 2)
samples = gauss1.rvs(size=100, random_state=12)

x = np.linspace(5, 8, 1000)

plt.plot(x, gauss1.pdf(x), color='black', linewidth=4, label='distribution')
plt.hist(samples, density=True, alpha=0.2, bins=10, edgecolor='black', label='sample')
plt.legend()
plt.show()

