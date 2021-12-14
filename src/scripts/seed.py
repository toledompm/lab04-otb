import mysql.connector
import uuid
from random import randint

conn = mysql.connector.connect(
    host="db", port="3306", user="dba", password="dba", database="test"
)

cursor = conn.cursor(prepared=True)

createTable = """
CREATE TABLE IF NOT EXISTS random_data (
    random_string varchar(25),
    random_number int(3)
)
"""

cursor.execute(createTable)

stmt = "INSERT INTO random_data (random_string, random_number) VALUES (%s, %s)"

for i in range(0, 300000):
    random_string = str(uuid.uuid4())[:25]
    random_number = randint(0, 100)
    cursor.execute(stmt, (random_string, random_number))

conn.commit()
conn.close()
