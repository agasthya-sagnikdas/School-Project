def PUSH():
    ele = int(input("Enter the element which you want to push:"))
    Stack.append(ele)

def POP():
    if Stack == []:
        print("Stack is Empty/Underflow")
    else:
        print("The deleted element is:", Stack.pop())

def PEEK():
    top = len(Stack) - 1
    print("The top most element of Stack is:", Stack[top])

def Disp():
    top = len(Stack) - 1
    print("The Stack elements are:")
    for i in range(top, -1, -1):
        print(Stack[i])

# Main Program
Stack = []
opt = 'y'

while opt == 'y' or opt == 'Y':
    print("Stack Operations")
    print("*****************")
    print("1. PUSH")
    print("2. POP")
    print("3. PEEK")
    print("4. Display")
    print("*****************")
    optn = int(input("Enter your choice:"))

    if optn == 1:
        PUSH()
    elif optn == 2:
        POP()
    elif optn == 3:
        PEEK()
    elif optn == 4:
        Disp()
    else:
        print("Invalid Input")

    opt = input("Do you want to perform another stack operation (y/n)?: ")
