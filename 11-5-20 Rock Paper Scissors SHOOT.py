# Jeremiah Allu
# 11-5-20
# Pd.5
# Rock, Paper, Scissors, Shoot

from random import *
seed()
playAgain='yes'
while playAgain.lower()=='yes' or playAgain.lower()=='yes':
    # Only checks lower case: .lower()
    print()
    print('Let\'s Play Rock Paper Scissors!')
    print('You must either enter, rock, paper, or scissors')
    print('Then the computer will randomly make its choice and print out the winner.')
    print()
    choice=input('What is your choice: ')
    print()


    # 1=Rock 2=Paper and 3=scissors
    compChoice=int(random()*3)+1
    if choice=='rock' or choice=='paper' or choice=='scissors':
        if choice=='rock':
            if compChoice==1:
                print('We both picked Rock. Tie!')
            elif compChoice==2:
                print('The computer picked paper. You lost. Paer cover Rock!')
            else:
                print('The computer picked scissors. You won. Rock smashes scissors!')
        elif choice=='paper':
            if compChoice==1:
                print('The computer picked rock. You won. Paper covers Rock!')
            elif compChoice==2:
                print('We both picked paper. Tie!')
            else:
                print('The computer picked scissors. You lost. Scissors cuts Paper!')
        else:
            if compChoice==1:
                print('The computer picked Rock. You lost. Rock smashes Scissors!')
            elif compChoice==2:
                print('The computer picked paper. You won. Scissors cuts Paper!')
            else:
                print('We both picked scissors. Tie!')
    else:
        print('You enter invalid data!')

    print()
    playAgain=input('Please enter yes or y to play again. Enter no to quit: ')
    print()
print()
print('Thanks for Playing!')
    
        


                    
                
