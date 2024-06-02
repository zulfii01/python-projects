import random

number_of_dice = input("Enter the number of dice : ")
for i in range(int(number_of_dice)):
    result = random.randint(1,6)
    print (result)
