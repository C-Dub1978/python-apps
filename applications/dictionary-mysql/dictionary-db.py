import mysql.connector
import os

file = os.path.abspath('../files/.env')
with open(file) as dataFile:
  data = dataFile.read()

def fetchQuery(str, connection):
  cursor = connection.cursor()
  sql = cursor.execute("SELECT word, definition FROM dictionary WHERE word = '%s' " % str)
  return cursor.fetchall()

def runInput(conn):
  results = fetchQuery('line', conn)
  for result in results:
    print(result)

try:
  print(mysql.connector)
  # Create connection
  connection = mysql.connector.connect(
    user=data,
    password=data,
    host = 'localhost',
    database = 'dictionary_schema'
  )
  runInput(connection)

except Exception as e:
  print('Error connecting to db, exiting program')
