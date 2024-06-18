import mysql.connector

# Establishing the connection
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

# Creating a cursor object
db = database.cursor()

# Inserting data into the table
sql = '''INSERT INTO `student2` (`Sn`, `Name`, `Physics`, `chemistry`) 
VALUES ('3', 'Nitin', '69', '42');'''
db.execute(sql)
database.commit()

# Fetching data from the table
db.execute("SELECT * FROM student2")
result = db.fetchall()

# Printing the result
for x in result:
    print(x)

#Inserting in other table of same database
import mysql.connector

# Connect to the MySQL database
database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="student"
)

# Creating a cursor object
db = database.cursor()

n = int(input("Enter n= "))
for i in range(1, n + 1):
    name = input("Enter name= ")
    physics = int(input("enter physics mark= "))
    maths = int(input("enter Maths mark= "))
    chemistry = int(input("enter chemistry mark= "))
    english = int(input("enter english mark= "))
    nepali = int(input("enter nepali mark= "))
    
    total = physics + maths + chemistry + english + nepali
    per = total / 5
    if per >= 80:
        grade = "A"
    elif per >= 70:
        grade = "B"
    elif per >= 60:
        grade = "C"
    elif per >= 45:
        grade = "D"
    else:
        grade = "Failed"
    
    sql = f'''INSERT INTO `student3` (`Sn`, `Name`, `physics`, `Maths`, `chmistry`, `english`, `nepali`, `total`, `per`, `grade`) 
              VALUES ('{i}', '{name}', '{physics}', '{maths}', '{chemistry}', '{english}', '{nepali}', '{total}', '{per}', '{grade}');'''
    
    db.execute(sql)

database.commit()
db.close()
