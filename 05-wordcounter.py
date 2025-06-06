file1=open("input-program5.txt","r")
line=" "
count=0
while line:
    line=file1.readline()
    s=line.split()
    for word in s:
        count+=1
print("Number of words=",count)
file1.close()