from random import *

roll = True
while (roll==True):
    print ("Let's roll the dice!")
    chosen_number = randrange(1,6)
    print ("The number rolled is: ", chosen_number)
    correct_input = False
    while (correct_input==False):
        roll_again = input("Would you like to roll again? [Enter 'Y' or 'y' for Yes; 'N' or 'n' for No]:")
        if (roll_again == 'Y' or roll_again == 'y'):
            correct_input = True
            roll = True
            break
        elif (roll_again == 'N' or roll_again == 'n'):
            correct_input = True
            roll = False
            break
        else:
            print ("You entered the wrong input!")
            correct_input = False
            continue
    if (roll == True):
        continue
    else:
        print ("Bye bye")
        break
