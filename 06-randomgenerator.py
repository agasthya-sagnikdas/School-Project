import random
while True:
    Choice = input("\nDo you want to roll the dice(y/n): ")
    no = random.randint(1,6)
    if Choice == 'y':
        print("\nYour Name is: ",no)
    else:
        break