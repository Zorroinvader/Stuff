import sqlite3
import json
import os 
os.remove('mydatabase.db')
# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('mydatabase.db')

# Create a cursor object
cursor = conn.cursor()

# Create a new table
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                  )''')
cursor.execute('''CREATE TABLE IF NOT EXISTS list (
    id INTEGER  PRIMARY KEY,
    data TEXT
    )'''
)
testinput = input("tset")

favapplist = ["Test","Test2","Test3" , testinput]
list_json = json.dumps(favapplist)
cursor.execute("INSERT INTO list (data) VALUES (?)", (list_json,))
conn.commit()
cursor.execute("SELECT * FROM list")
rows = cursor.fetchall()

retrievef_List = json.loads(rows[0][1])
print (retrievef_List)
# Commit the transaction
conn.commit()
conn.rollback()


cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John', 30))
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))

# Commit the transaction
conn.commit()

# Fetch data from the table
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()

# Print the fetched data
for row in rows:
    print(row)

# Close the database connection
conn.close()
