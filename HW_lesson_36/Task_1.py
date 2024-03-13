#Task 1
"""
Create a table

Create a table of your choice inside the sample SQLite database, rename it, and add a new column. Insert a couple rows inside your table. Also, perform UPDATE and DELETE statements on inserted rows.

As a solution to this task, create a file named: task1.sql, with all the SQL statements you have used to accomplish this task
"""

import sqlite3

conn = sqlite3.connect("data_base.db")
if conn:
    print("Connection to the PostgreSQL established successfully.")
else:
    print("Connection to the PostgreSQL encountered and error.")
print()
 
cursor = conn.cursor()




cursor.execute("CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY, name TEXT, age INTEGER);")
cursor.execute("ALTER TABLE my_table RENAME TO my_user_table;")
cursor.execute("ALTER TABLE my_table RENAME TO my_user_table;")
cursor.execute("ALTER TABLE my_user_table ADD COLUMN  phone INTEGER;")
cursor.execute("INSERT INTO my_user_table (name, age, phone) VALUES ('John', 30, '545646465');")
cursor.execute("INSERT INTO my_user_table (name, age, phone) VALUES ('Alice', 25, '5451541445');")
cursor.execute("UPDATE my_user_table SET age = 31 WHERE name = 'John';")
cursor.execute("DELETE FROM my_user_table WHERE name = 'Alice';")
cursor.execute("SELECT * FROM my_user_table;")

print(f"Data in the table my_user_table:")
data = cursor.fetchmany(10)
for row in data:
    print(row)
    
print()

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables in the database:")
for table in tables:
    print(table[0])


conn.close()
