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