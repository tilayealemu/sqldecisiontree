import csv
import sys

import MySQLdb

dbServer = sys.argv[1]
dbName = sys.argv[2]
dbUser = sys.argv[3]
dbPass = sys.argv[4]
dbQuery = sys.argv[5]

db = MySQLdb.connect(host=dbServer, user=dbUser, passwd=dbPass, db=dbName)
cursor = db.cursor()
cursor.execute(dbQuery)

with open("training.csv", "wb") as file:
    writer = csv.writer(file)
    writer.writerow([i[0] for i in cursor.description])
    writer.writerows(cursor)
