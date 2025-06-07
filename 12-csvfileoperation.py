import csv

def Create():
    F = open("Emp.csv", 'a', newline='')
    W = csv.writer(F)
    opt = 'y'
    while opt == 'y':
        No = int(input("Enter Employee Number: "))
        Name = input("Enter Employee Name: ")
        Sal = float(input("Enter Employee Salary: "))
        L = [No, Name, Sal]
        W.writerow(L)
        opt = input("Do you want to continue(y/n)?: ")
    F.close()

def Search():
    F = open("Emp.csv", 'r', newline='\r\n')
    no = int(input("Enter Employee number to search: "))
    found = 0
    row = csv.reader(F)
    for data in row:
        if data[0] == str(no):
            print("\nEmployee Details are:")
            print("---------------------")
            print("Name:", data[1])
            print("Salary:", data[2])
            print("=====================")
            found = 1
            break

    if found == 0:
        print("The searched Employee number is not found")
    F.close()

Create()
Search()
