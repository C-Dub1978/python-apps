import time
import os
import pandas

# while True:
#   with open('./files/names.txt', 'r') as myFile:
#     print(myFile.read())
#     time.sleep(10)

# What if we wanted to run the above script, but wante to
# make sure that the file exists first.... we can use the os module for this

# while True:
#   if os.path.exists('./files/names.txt'):
#     with open('./files/names.txt', 'r') as myFile:
#       print(myFile.read())
#   else:
#     print('File does not exist...')
#   time.sleep(5)

# 3rd party modules!!!!!!!!!!
 # to install 3rd party modules, we use pip.....
 # pip3 install someModule  >>> note - anything after 3.9 you would use its version like pip3.10 install blahBlah

# we will read the csv file with pandas, its got a bunch of modules for reading data

while True:
  if os.path.exists('./files/temps_today.csv'):
    data = pandas.read_csv('./files/temps_today.csv')
    print(data.mean()["st1"])
  else:
    print('File not found...')
  time.sleep(5)