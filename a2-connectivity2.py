import mysql.connector

con = mysql.connector.connect(
    host='localhost',
    username='root',
    password='Geek4all@123',
    database='employees'
)

if con.is_connected():
    cur = con.cursor()
    opt = 'y'
    while opt == 'y':
        No = int(input("Enter Employee Number:"))
        Name = input("Enter Employee Name:")
        Gender = input("Enter Employee Gender (M/F):")
        Salary = int(input("Enter Employee Salary:"))
        Query = "INSERT INTO EMP VALUES({}, '{}', '{}', {})".format(No, Name, Gender, Salary)
        cur.execute(Query)
        con.commit()
        print("Record Stored Successfully")
        opt = input("Do you want to add another employee details(y/n):")

Query = "SELECT * FROM EMP"
cur.execute(Query)
data = cur.fetchall()
for i in data:
    print(i)

con.close()
