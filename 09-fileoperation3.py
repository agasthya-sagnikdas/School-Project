F1 = open("Sample.txt", 'r')
F2 = open("New.txt", 'w')
while True:
    line = F1.readline()
    if line == '':
        break
    if line[0] == 'a' or line[0] == 'A':
        F2.write(line)

print("All lines which are starting with character 'a' or 'A' has been copied successfully into New.txt")
F1.close()
F2.close()