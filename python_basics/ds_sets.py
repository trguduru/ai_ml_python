# example usage of Set data structure
countries_dup = ['India', 'US', 'India', 'Japan']

print(countries_dup)

countries = set(countries_dup)  # creating a set from a list
print(countries)

countries.add('UK')  # adding an element

print(countries)

# removed a random element
removed = countries.pop()
print(removed)
print(removed in countries)  # false, removed element is not existed

# removed a specific element
countries.remove('UK')
print(countries)

# additional set operations
