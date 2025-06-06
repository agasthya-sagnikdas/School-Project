f = open("Story.txt", 'r')
Contents = f.read()
Vowels = 0
Consonants = 0
Lower_case = 0
Upper_case = 0

for ch in Contents:
    if ch in 'aeiouAEIOU':
        Vowels = Vowels + 1
    if ch in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
        Consonants = Consonants + 1
    if ch.islower():
        Lower_case = Lower_case + 1
    if ch.isupper():
        Upper_case = Upper_case + 1

f.close()

print("The total numbers of vowels in the file:", Vowels)
print("The total numbers of consonants in the file:", Consonants)
print("The total numbers of uppercase in the file:", Upper_case)
print("The total numbers of lowercase in the file:", Lower_case)