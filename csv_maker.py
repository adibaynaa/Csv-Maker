
from datetime import datetime

import csv

# lst = []

nowDate = datetime.now().strftime('%D')
nowTime = datetime.now().strftime('%H: %M: %S')

filename = 'gaoTek.csv'

with open(filename, 'w', newline="") as file:
  csvWriter= csv.writer(file)
  while True:
    inp = input('Name: ')
    if inp== 'x' or len(inp)<4:
      break

    else:
      cell = input('Phone Number: ')
      mail= input('Email: ')
      dept= input('Department: ')
      joinDate= input('Joining Date: ')
      endDate= input('Ending Date: ')

      csvWriter.writerow([nowDate, nowTime, inp, cell, mail, dept, joinDate, endDate])

file.close()