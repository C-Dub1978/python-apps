import mysql.connector
import os
import difflib
from difflib import SequenceMatcher

file = os.path.abspath('../files/.env')
with open(file) as dataFile:
  data = dataFile.read()

def runInput(searchWord):
  sql = cursor.execute("SELECT word, definition FROM dictionary WHERE word = '%s' " % searchWord)
  return cursor.fetchall()

def printResults(results):
  print(results)
  print()

def lookup(key):
  if key.upper() in allWords:
    return runInput(key.upper())
  if key in allWords:
    return runInput(key)
  else:
    matches = difflib.get_close_matches(key, allWords)
    caseInsensitive = False
    foundKey = ""

    if len(matches) > 0:
      for match in matches:
        if str(match).upper() == key.upper():
          caseInsensitive = True
          foundKey = str(match)
          break
      if caseInsensitive == True:
        print(foundKey)
        return runInput(foundKey)
      else:
        confirmation = input('No matches for the word you entered, did you mean: ' + matches[0] + '?\nPress 1 for yes, 2 for no: ')
        if confirmation == '1':
          return runInput(matches[0])
        elif confirmation == '2':
          return 'No matches found'
        else:
          return 'No matches found'
    else:
      return 'No matches found for the word you entered, please check the spelling and try again'

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
  words = cursor.fetchall()
  allWords = []
  for w in words:
    word = str(w)
    stripped = str(word[2:len(word) - 3])
    allWords.append(stripped)

  while True:
    word = input('Enter word to search for , or type stop to exit the program: ')
    if word.upper() == 'STOP':
      break
    else:
      results = lookup(word)
      if results is not None:
        printResults(results)
      else:
        print('No results found for that word, please try again.\n')

except Exception as e:
  print('Error connecting to db, exiting program')
