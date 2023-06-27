# examples explaining the uniform distribution,
# see https://docs.scipy.org/doc/scipy/tutorial/stats/continuous_uniform.html

import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt

u = uniform(loc=10, scale=5)
print(u.pdf([10, 8, 11, 15]))

upoints = np.linspace(8, 17, 1000)  # split the values into the given number, which is 100 here
ppoints = u.pdf(upoints)  # the distribution of the above points
plt.plot(upoints, ppoints)  # this one explains whether the distribution is uniform or not
# plt.show()

print(u.mean())  # mean of the distribution

print(u.rvs())  # random variates - sample, this is a single sample
print(u.rvs(size=5))  # returns 5 sample of the distribution
plt.hist(u.rvs(size=1000), density=True)  # show the uniform distribution of the sampling
plt.show()




print(u.cdf(12))