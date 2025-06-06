First = 0
Second = 1
no = int(input("How many Fibonacci numbers you want to display? "))
if no <= 0:
    print("Please Enter Positive Integer")
else:
    print(First)
    print(Second)
    for i in range(2,no):
        Third = First + Second
        First = Second
        Second = Third
        print(Third)