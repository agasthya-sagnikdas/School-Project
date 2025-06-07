import mysql.connector

con = mysql.connector.connect(host='localhost',
                              username='root',
                              password='Geek4all@123',
                              database='employees')

if con.is_connected():
    cur = con.cursor()
    print("************************")
    print("Welcome to Employee Search Screen")
    print("************************")
    No = int(input("Enter the employee number to search:"))
    Query = "SELECT * FROM EMP WHERE No={}".format(No)
    cur.execute(Query)
    data = cur.fetchone()
    if data != None:
        print(data)
    else:
        print("Record not Found!!!")

con.close()
