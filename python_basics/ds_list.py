# this contains the example for List data structure
names = []
#print(names[0])  # throws error
names = ["Reddy","Hansi","Hanish"]
print(names[0])  # first element
print(names[-1])   # negative means starting from the end , -1, -2 , -3 etc ...

# a list contain heterogeneous values like below
heteroList = [1, True, "Awesome", 3.5]
print(heteroList[0])
print(heteroList[-1])
print(heteroList[2])

print(len(heteroList))   # list length


# slicing of a list

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
print(months[3:5])  # lower inclusive , upper exclusive
print(months[:5])   # all until index 5
print(months[5:])   # all until end of the list from index 5

# list 'in' and 'not  in'  functions

print('May' in months, 'Day' not in months)  # the above slice, in and not in works for string  values as well
print('Day' in "Sun Day",  'May' not in "Sun Day")


# list methods

print(len(months))  # return the length of the list
print(max(months))  # returns the max value after string
print(min(months))  # returns the  smallest in the sorted list, means it will sort first then return the 0 index
print(sorted(months))

student_ages = [10, 14, 21, 18, 50,4]
print(max(student_ages))
print(min(student_ages))
print(sorted(student_ages))

#  join  method

weekdays = ["Monday", "Tuesday","Wednesday", "Thursday", "Friday"]
weekend_days = ["Saturday", "Sunday"]

print(" Hot ".join(weekdays))

#  append, adds at  the end of the list

weekdays.append("Sunday")  # + also can be used to append at the end of the list
print(weekdays[5])  # return Sunday which was append in the above statement

# delete from list
del(weekdays[-1])  # deletes last element, or provide an index to delete
print(weekdays)

# replace an element in the list
print("Replacing an element in the list")
print(weekdays)
weekdays[0] = "Great Start Day"
print(weekdays)

# print the index of a value
print(weekdays.index('Wednesday'))

