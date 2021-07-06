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

# tuples
# they are simply a list of comma seperated values, of any/all/mixed data types. They are IMMUTABLE
myTup1 = (1, 2, "some", "value")
myTup2 = (3.3, "string", { "prop1": 2}, 3)
# remember if you create a tuple with ONLY 1 value, you must add a comma
myTup3 = (1,)
print("Tuple 1: ", myTup1)
print("Tupel 2: ", myTup2)
print("Tuple 3: ", myTup3)
print()

# useful - if you call dir(str), dir(float), dir(int), dir(dict) etc, you can see the attributes of that
# data type, which are similar to javascript prototypes

# Dictionaries - think javascript objects
grades = { "ethan": 10.0, "finn": 8.3, "oliver": 8.1 }

# Mutating lists - be aware that calling default functions on lists will mutate them.
firstList = [1, 2, 3]
secondList = [2, 3, 4]
secondList.append(5)
print(secondList)

# Accessing a list slice - first number before colon is inclusive, second after colon is exclusive
listSlice1 = [1, 2, 3, 4, 5, 6, 7]
listSlice2 = listSlice1[1:3]
print(listSlice2)
# If starting from list index 0, you don't have to specify, you can use varName[:3] for example
# You can also omit the second number if you want python to check through end of list varName[1:]

# Accessing lists with negative indeces
# Python also assigns each item in a list a negative index - the end of the list is index -1, the second from end -2, etc
negativeList = [1, 2, 3, 4, 5, 6]
print("Negative index: ", negativeList[-2:]) # This would give us the last 2 items (5, 6) since we arent specifying an end in the slice
print("Negative index slice: ", negativeList[-4:-2]) # prints [3, 4] since index -2 is exclusive

# Keep in mind, strings have the exact same indexing system just like lists, with slices, negative indeces, etc

# Dictonaries have indexing that corresponds to the actual key - similar to javascript object notation but without the dot notation js has
dictKey1 = { "one": 1, "two": 2 }
print(dictKey1["one"])

