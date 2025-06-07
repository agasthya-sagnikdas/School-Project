n = int(input("Enter a number to check: "))
n1 = n
s = 0
while(n>0):
    d = n % 10
    s = s + (d * d * d)
    n = int(n/10)
if s == n1:
    print("Armstrong Number!")
else:
    print("Not an Armstrong Number!")