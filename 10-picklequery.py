import pickle

def Create():
    F = open("Students.dat", 'ab')
    opt = 'y'
    while opt == 'y':
        Roll_No = int(input("Enter roll number: "))
        Name = input("Enter Name: ")
        L = [Roll_No, Name]
        pickle.dump(L, F)
        opt = input("Do you want to add another student detail(y/n): ")
    F.close()

def Search():
    F = open("Students.dat", 'rb')
    no = int(input("Enter Roll.No of student to search: "))
    found = 0
    try:
        while True:
            S = pickle.load(F)
            if S[0] == no:
                print("The searched Roll.No is found and Details are:", S)
                found = 1
                break
    except:
        F.close()

    if found == 0:
        print("The Searched Roll.No is not found")

Create()
Search()