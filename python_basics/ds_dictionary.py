# examples for dictionary data type
student_agents = {"Ram": 10, "Bheem": 11, "Krishna": 8}

print(student_agents["Ram"])
print(student_agents.get("Ram"))

# update Krishna's age
krisha_age = {"Krishan": 10}

student_agents.update(krisha_age)

print(student_agents)
