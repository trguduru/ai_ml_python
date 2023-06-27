# simple pandas package usage
import pandas as pd

print(pd.Series([10, 15, 20]))

students = pd.Series([10, 20, 30, 40, 50])
print(students)
print("Series min:", students.min())

# series to array
print("Series to Array:", students.array)

print("Series Transpose :", students.T)

print("Series dimension: ", students.ndim)

print("Series plot: ", students.plot)


print(students.sum())
