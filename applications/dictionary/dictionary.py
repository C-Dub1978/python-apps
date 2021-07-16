import json
import difflib
from difflib import SequenceMatcher

dictionaryData = json.load(open('./files/data.json'))

def lookup(key):
  if key in dictionaryData:
    return (dictionaryData[key])[0]
  else:
    matches = difflib.get_close_matches(key, dictionaryData.keys())
    if len(matches) > 0:
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