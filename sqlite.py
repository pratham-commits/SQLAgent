import sqlite3

## connect to sqlite

connection=sqlite3.connect("student.db")

## create a cursor object to insert record and create table
cursor= connection.cursor()

## create table

table_info="""
create table STUDENT(NAME VARCHAR(25), DIVISION VARCHAR(25) , GROUPNAME VARCHAR(25), MARKS INT)
"""
cursor.execute(table_info)

## insert some records

students = [
    ("Riya", "A", "Science", 89),
    ("Aman", "B", "Commerce", 76),
    ("Neha", "A", "Arts", 92),
    ("Raj", "C", "Science", 65),
    ("Simran", "B", "Commerce", 81)
]

insert_query = "insert into STUDENT (NAME, DIVISION, GROUPNAME, MARKS) VALUES (?, ?, ?, ?)"
cursor.executemany(insert_query, students)

## display all the records

print("The inserted records are:-")

data=cursor.execute("Select * from Student")
for row in data:
    print(row)
    
##closing

connection.commit()
connection.close()

