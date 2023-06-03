# demonstrates the use of while loop

x = 123
while x > 10:
    x = x % 10
    print(x)


# demonstrates the for loop

ages = [10, 12, 23, 24, 25]
for age in ages:
    print(age)

student_agents = {"Ram": 10, "Bheem": 11, "Krishna": 8}

for name, age in student_agents.items():  # items returns an iterator to loop through, key firs and then value
    print(name,age)

