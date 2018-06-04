import sqlite3

# Basics
db = sqlite3.connect("cookies")
cursor = db.cursor() 
cursor.execute("select host_key from cookies limit 10") # sqlite3.connect("cookies").cursor.execute("query")
results = cursor.fetchall()
print(results)
db.commit()
db.close()

