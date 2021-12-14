import mysql.connector
import os

IS_PREPARED = os.getenv("IS_PREPARED")

print("Executing with IS_PREPARED?", IS_PREPARED != None)

conn = mysql.connector.connect(
    host="db", port="3306", user="dba", password="dba", database="test"
)

cursor = conn.cursor(prepared=(IS_PREPARED != None))

for i in range(0, 1000):
    if IS_PREPARED:
        stmt = "SELECT count(*) FROM random_data where random_number = %s"
        cursor.execute(stmt, (i,))
    else:
        stmt = "SELECT count(*) FROM random_data where random_number = '%s'" % (i)
        cursor.execute(stmt)

    for count in cursor:
        pass

conn.close()
