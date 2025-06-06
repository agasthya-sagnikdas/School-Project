import mysql.connector
con = mysql.connector.connect(host='localhost',
                              username='root',
                              password='Geek4all@123',
                              database='employees')
if con.is_connected():
    cur = con.cursor()
    print("**************************************")
    print("Welcome to Employee detail update Screen")
    print("**************************************")
    No = int(input("Enter the employee number to Update:"))
    Query = "SELECT * FROM EMP WHERE No={}".format(No)
    cur.execute(Query)
    data = cur.fetchone()
    if data != None:
        print("Record found details are:")
        print(data)
        ans = input("Do you want to update the Salary of the above employee (y/n)?:")
        if ans == 'y' or ans == 'Y':
            New_Sal = int(input("Enter the New Salary of an Employee:"))
            Q1 = "UPDATE EMP SET SALARY={} WHERE No={}".format(New_Sal, No)
            cur.execute(Q1)
            con.commit()
            print("Employee Salary Updated Successfully")
            Q2 = "SELECT * FROM EMP"
            cur.execute(Q2)
            data = cur.fetchall()
            for i in data:
                print(i)
    else:
        print("Record not Found!!!")
