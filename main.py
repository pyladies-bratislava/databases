import sqlite3

connection = sqlite3.connect("music.db")
cursor = connection.cursor()

# Exercise 1
sql = "SELECT COUNT(*) FROM artists;"
cursor.execute(sql)
result = cursor.fetchone()
print(f"There are {result[0]} artists in your database.")

# Exercise 2
sql = "SELECT COUNT(*) FROM tracks;"
cursor.execute(sql)
result = cursor.fetchone()
print(f"There are {result[0]} tracks in your database.")

# Exercise 3
sql = "SELECT name FROM media_types;"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row[0])

# Exercise 5
sql = "SELECT artistid from artists WHERE name = 'U2';"
cursor.execute(sql)
result = cursor.fetchone()
u2_artistid = result[0]
print(f"The artistid for U2 is {u2_artistid}.")

sql = f"SELECT albumid, title from albums WHERE artistid = {u2_artistid};"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)

# Close everything
cursor.close()
connection.close()