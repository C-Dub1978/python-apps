# If you have a function that doesn't return a value and just has side effects, make sure to return None (literally the word none)
# Its just best practice to always return something in your functions, including the None type
# Note - for comparison operators, instead of using &&, use the word 'and', and instead of || use 'or'
# if x == 1 and y == 1.....
# if x == 1 or y == 3.....
# 1 more thing to keep in mind, True is a data type in python, as is False
def noneFunc():
    useless = 2 + 1
    print("Useless")
    return None

print(noneFunc())

# Conditionals 1 - keep indenting inside conditional statements
def findMean(value):
    # Simple if/else block
    # The below line is using type() function, its actually better practice to us isinstance() function
    # if type(value) == list:
    if isinstance(value, list):
        return sum(value) / len(value)
    else:
        return sum(value.values()) / len(value)

print("Mean with list is: ", findMean([1, 2, 3, 4, 5]))
print("Mean with dictionary is: ", findMean({ "one": 1, "two": 2, "three": 3}))

# User input , use the input function and remember it blocks execution
def checkNumber():
    tempInput = input('Please enter a temperature: ')
    if float(tempInput) > 75:
        return 'Hot'
    else:
        return 'Cold'

# print(checkNumber())

# For loops
todaysTemps = [65.4, 78.9, 55.7]
for temp in todaysTemps:
    print(round(temp))

    # looping through dictionary
mydic = { "me": "awesome", "you": "lame", "they": "half decent" }
for n in mydic.keys():
    print(mydic[n])

# While loops
username = ""
while username != "chris":
    print('Not Chris')
    username = input('Enter your name: ')

    # While loop break and continue
while True:
    u = input('What is your name? ')
    if u == "Chris":
        break
    else:
        continue

# List comprehensions
# Lets say we have a list of numbers, we want to divide each by 10, but dont want to iterate in a regular for loop
# With list comprehensions, we can define a new var and set its value to a new list while iterating through the
# original all in one line of code
tempsForToday = [221, 330, 65, 102]

# instead of iterating with a list, lets create a new list with comprehension
newTempsForToday = [temp / 10 for temp in tempsForToday]
print("Todays temps before comprehension: ", tempsForToday)
print("After comprehension: ", newTempsForToday)
print()

# List comprehension can also have conditionals in them
newerTempsForToday = [temp / 10 for temp in tempsForToday if temp < 300]
print("After comprehension with conditional: ", newerTempsForToday)
print()

# List comprehension with multiple conditionals (just make sure the for loop syntax is AFTER the if/else)
evenNewerTemps = [temp / 10 if temp < 300 else 99999 for temp in tempsForToday]
print("After if/else comprehension: ", evenNewerTemps)

# Functions
# Functions can take values, or 'keyword arguments'
# note the following
# def myFunc(a, b):
    # return a * b

# to call the above, you can pass values myFunc(4, 5)
# or you can pass keyword arguments myFunc(a = 4, b = 5)
# and you can also mix up the order of the keword args as long as they match the function args myFunc(b = 5, a = 4)

# You can also assign default args values
# def myFunc(a = 4, b = 5):
    # return a * b

# then call with or without args myFunc()  or   myFunc(4)   or myFunc(b = 3)

# REMEMBER - you cannot have a non-default arg in a function before a default arg
# def myFunc(a, b = 5) ERROR

# Indefinite number of args (average function for example)
# def myFunc(*whatever):
  # return sume(whatever) / len(whatever)

# Indefinite number of keyword arguments (2 asterisk instead of 1)
# def myFunc(**whatever):
    # return whatever

# print(myFunc(arg1 = 1, arg2 = 2, arg3 = 3)) --- in this case the myFunc will return a dictionary of
# arg names and their values { arg1: 1, arg2: 2, arg3: 3}

