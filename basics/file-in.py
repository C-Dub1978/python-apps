# Open/Read basics
myFile = open("./files/fruits.txt")
print(myFile.read())
# In the above, the cursor defaults to being right before the very
# first character, and after the first read operation, it ends up
# just after the very last character. If you call file.read() again, it
# outputs the empty string
print(myFile.read())
# close it
myFile.close()

# you can store the results of a read op in a variable
newFile = open("./files/fruits.txt")
contents = newFile.read();
print(contents)
print(contents)
newFile.close()

# There is a cleaner way to do the above..... (open, read, then close)
# the with context manager will automatically close the file after it sees the non-indent
# after line 23
with open("./files/fruits.txt", 'r') as withFile:
  newContent = withFile.read()

print(newContent)

# Writing - if the file to write to already exists, it will override the contents,
# so use a newline character to append to it
with open('./files/names.txt', 'w') as namesFile:
  namesFile.write('Scott\nAmy\nElton\nJoe\n')

# Writing with appending instead of overwriting
with open('./files/names.txt', 'a') as namesUpdate:
  namesUpdate.write('update1\nupdate2\nupdate3\n')

# To see different modes of opening files, just use the interpreter and help(open)

# To write then read
with open('./files/names.txt', 'a+') as namesRW:
  namesRW.write('write1\nwrite2\nwrite3\n')
  # the seek function tells you where to automagically move the cursor
  namesRW.seek(0)
  testContent = namesRW.read()

print(testContent)


