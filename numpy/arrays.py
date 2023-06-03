
# examples using numpy package , numeric python for arrays and also methods for linear algebra etc...

import numpy as np

# single dimension array
ages = [10, 14, 20]

ages_array = np.array(ages)

print(ages_array)

names = ["Ram", "Bheem", "Krishna"]

# 2D array example

student_ages = [names, ages]

print(student_ages)

student_ages_array = np.array(student_ages)

print("Student 2D Array : ", student_ages_array)

print(student_ages_array.shape)

print(student_ages_array[1, 0])  # print the value 2D array cell

print(student_ages_array[0])

print(student_ages_array[0:2, 1:3])

#  looping 1D array

for age in ages:
    print(age)

#  looping 2D array

for age in np.nditer(student_ages_array[1]):  # age is the second row in the 2D array
    print(age)
for name in np.nditer(student_ages_array[0]):  # prints the first row
    print(name)


