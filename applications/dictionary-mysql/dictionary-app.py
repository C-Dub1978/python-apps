import pymysql
import os
import pymysql.cursors

file = os.path.abspath('../files/.env')
with open(file) as dataFile:
  data = dataFile.read()

try:
  connect = pymysql.connect(
  host='localhost',
  user=data,
  password=data,
  database='dictionary_schema',
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
  )
  print('Successfully connected to db')
except Exception as e:
  print('Error connecting to db')