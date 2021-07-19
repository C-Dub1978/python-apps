import pymysql
import pymysql.cursors
import os
import json
import getpass
from threading import Thread

def writeTable(connect):
  with connect:
    with connect.cursor() as cursor:
      # Drop db schema
      db = "DROP DATABASE IF EXISTS `dictionary_schema`"
      cursor.execute(db)
      # Recreate db schema
      dbCreate = "CREATE DATABASE `dictionary_schema`"
      cursor.execute(dbCreate)
      # Use new schema
      use = "USE `dictionary_schema`"
      cursor.execute(use)
      # Drop table if exists
      drop = "DROP TABLE IF EXISTS `dictionary`"
      cursor.execute(drop)
      # Create dictionary table`
      create = ("CREATE TABLE `dictionary` ("
      +"`id` int(11) NOT NULL AUTO_INCREMENT,"
      +"`word` varchar(255) COLLATE utf8_bin NOT NULL,"
      +"`definition` varchar(10000) COLLATE utf8_bin NOT NULL,"
      +"PRIMARY KEY (`id`)"
      +")"
      +" ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin AUTO_INCREMENT=1;")
      cursor.execute(create)
      # Read in the json data, the file is one dir above
      file = os.path.abspath("../files/data.json")
      data = json.load(open(file))
      print("Please wait while data is written")
      # Loop through dictionary, and write the word and its meaning to the dictionary table
      for k in data.keys():
        word = k
        res = data[word]
        # A word can be mapped to a list of multiple definitions, if so, write a new db row for
        # each definition
        if len(res) > 1:
          for d in res:
            insert = "INSERT INTO dictionary (word, definition) VALUES (%s, %s)"
            cursor.execute(insert, (word, d))
        # The word only has 1 definition, write 1 row and move on
        else:
          definition = data[word][0]
          insert = "INSERT INTO dictionary (word, definition) VALUES (%s, %s)"
          cursor.execute(insert, (word, definition))
      connect.commit()
      print('\nSuccess! Dumped json data to dictionary table')

# connect with uname/pass
username = input('Enter mysql username: ')
password = getpass.getpass('Enter mysql password: ')

try:
  connection = pymysql.connect(
    host='localhost',
    user=username,
    password=password,
    database='dictionary_schema',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
  )
  print('successful connection!')
  writeTable(connection)

except Exception as e:
  print('Error with database operations')
  print(e)
