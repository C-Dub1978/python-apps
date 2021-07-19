import mysql.connector
import os

file = os.path.abspath('../files/.env')
with open(file) as dataFile:
  data = dataFile.read()

def runInput(searchWord):
  sql = cursor.execute("SELECT word, definition FROM dictionary WHERE word = '%s' " % searchWord)
  return cursor.fetchall()

def printResults(results):
  print(results)
  print()

try:
  # Create connection
  connection = mysql.connector.connect(
    user=data,
    password=data,
    host = 'localhost',
    database = 'dictionary_schema'
  )
  cursor = connection.cursor()
  ws = cursor.execute("SELECT word FROM dictionary")
  allWords = cursor.fetchall()
  print('ALL WORDS')
  print(allWords)

  while True:
    word = input('Enter word to search for , or type stop to exit the program: ')
    if word.upper() == 'STOP':
      break
    else:
      results = runInput(word)
      if results is not None:
        printResults(results)
      else:
        print('No results found for that word, please try again.\n')

except Exception as e:
  print('Error connecting to db, exiting program')
