def Factorial(no):
    F = 1
    if no < 0:
        print("Sorry, we cannot take Factorial for Negative number")
    elif no == 0:
        print("The Factorial of 0 is 1")
    else:
        for i in range(1, no + 1):
            F = F * i
        print("The Factorial of", no, "is:", F)

def Sum_List(L):
    Sum = 0
    for i in range(len(L)):  # use length of the list
        Sum = Sum + L[i]
    print("The Sum of List is:", Sum)

# Main Program
print("1. To Find Factorial")
print("2. To Find sum of List elements")
opt = int(input("Enter your choice: "))

if opt == 1:
    n = int(input("Enter a number to find Factorial: "))
    Factorial(n)

elif opt == 2:
    L = []
    n = int(input("Enter how many elements you want to store in List?: "))
    for i in range(n):
        ele = int(input(f"Enter element {i+1}: "))
        L.append(ele)
    Sum_List(L)

else:
    print("Invalid Option. Please enter 1 or 2.")
