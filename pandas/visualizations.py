# example usages of pandas dataframe APIs
import pandas as pd
import matplotlib.pyplot as plt

plt.close("all")

df = pd.DataFrame({'mass': [0.330, 4.87, 5.97], 'radius': [2439.7, 6051.8, 6378.1]},
                  index=['Mercury', 'Venus', 'Earth'])
plot = df.plot.pie(y='radius', figsize=(5, 5))
plt.show()  # shows the data visualization
