seconds = 60
minutes = seconds * 60
hours = minutes * 60
day = hours * 24
week = day * 7
print("There are ", week, " seconds in a week")
print("")

# python types are inferred, not strictly typed
x = 10 # int
y = "10" # string
z = 10.1 # float

#list
myList = [1, 2, 3]

#range
myRange = list(range(0, 11)) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> the upper num is exclusive
mySteppedRange = list(range(0, 11, 2)) # [0, 2, 4, 6, 8, 10] -> 3rd arg is a step
print(myList)
print(myRange)
print(mySteppedRange)

# useful - if you call dir(str), dir(float), dir(int), dir(dict) etc, you can see the attributes of that
# data type, which are similar to javascript prototypes

# Dictionaries - think javascript objects
grades = { "ethan": 10.0, "finn": 8.3, "oliver": 8.1 }
