f = open("Story.txt", 'r')
Contents = f.readlines()
for line in Contents:
    words = line.split()
    for i in words:
        print(i+'#', end=' ')
    print("")
f.close()