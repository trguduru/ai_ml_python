
# variable assignment
x,y,z = 5,10,15
print(x)
print(y)
print(z)

# assignment operator

bank_balance = 1000
# adding a credit of $500 and debit of $200
bank_balance += 500 - 200
print(bank_balance)


# data types and conversions

#  numeric type int,float
x = 100
print(x)
print(int(49.5))
print(float(4/2))

# the following will outputs as 0.30000000000000004 not 0.3 as python floats are approximates
print(0.1+0.1+0.1)

x = int(5.5)
y = float(10)
print(x,y)
print(type(x), type(y))

# booleans , comparison
x = 10
print(x > 10)


# strings
print("its a string")
print('its the same string')
firstName = "Ram"
lastName = "Dasarath"
print(firstName + " " + lastName)
print(firstName * 2)  # repeats Ram twice
print(len(firstName))
print(" Your\'s Name is awesome")  # string escaping
print("wonderful nation of the world".title())  # returns - Wonderful Nation Of The World

# Types & Type Conversion

print(type(1), type("1"), type(1.0))

mon_sales = "100"
print(type(mon_sales))

print(int(mon_sales) + int(mon_sales))




