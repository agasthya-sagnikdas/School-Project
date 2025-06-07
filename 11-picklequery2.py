import pickle

def Create():
    F = open("Marks.dat", 'ab')
    opt = 'y'
    while opt == 'y':
        Roll_No = int(input('Enter roll number:'))
        Name = input("Enter Name:")
        Mark = int(input("Enter Marks:"))
        L = [Roll_No, Name, Mark]
        pickle.dump(L, F)
        opt = input("Do you want to add another student detail(y/n):")
    F.close()

def Update():
    F = open("Marks.dat", 'rb+')
    no = int(input("Enter Student Roll.No to modify marks:"))
    found = 0
    try:
        while True:
            Pos = F.tell()
            S = pickle.load(F)
            if S[0] == no:
                print("The searched Roll.No is found and Details are:", S)
                S[2] = int(input("Enter New Mark to be updated:"))
                F.seek(Pos)
                pickle.dump(S, F)
                found = 1
                F.seek(Pos)  # moving the file pointer again to beginning of the current record
                print("Mark updated Successfully and Details are:", S)
                break
    except:
        F.close()

    if found == 0:
        print("The Searched Roll.No is not found")

# Main Program
Create()
Update()