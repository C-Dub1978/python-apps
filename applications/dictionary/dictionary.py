import json
import difflib
from difflib import SequenceMatcher
import os

file = os.path.abspath('../files/data.json')
dictionaryData = json.load(open(file))
print(dictionaryData['USA'][0])

def lookup(key):
  if key.upper() in dictionaryData:
    return (dictionaryData[key.upper()][0])

  if key in dictionaryData:
    return (dictionaryData[key])[0]
  else:
    matches = difflib.get_close_matches(key, dictionaryData.keys())
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
        return dictionaryData[foundKey][0]
      else:
        confirmation = input('No matches for the word you entered, did you mean: ' + matches[0] + '?\nPress 1 for yes, 2 for no: ')
        if confirmation == '1':
          return ''.join(dictionaryData[matches[0]])
        elif confirmation == '2':
          return 'No matches found'
        else:
          return 'No matches found'
    else:
      return 'No matches for the word you entered, please check the spelling.'



while True:
  word = input('Enter word to search for, or type the word stop to exit: ')
  if word.upper() == 'STOP':
    break
  else:
    result = lookup(word.lower())
    print(result + '\n')