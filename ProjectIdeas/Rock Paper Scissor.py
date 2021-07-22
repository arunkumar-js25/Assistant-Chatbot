import random
from prettytable import PrettyTable

def makePrettyTable(user,table_col1, table_col2, table_col3):
    table = PrettyTable()
    table.add_column("Round/Player", table_col1)
    table.add_column("CPU", table_col2)
    table.add_column(user, table_col3)
    return table

user = input("Enter Your Name to start the game: ").capitalize()
while True:
    signs = ['Rock','Paper','Scissors']
    GameBoard = [['Round 1','Round 2','Round 3'],['','',''],['','','']]
    userwin = 0
    CPUwin = 0

    for x in range(0,3):
        CPUturn = random.choice(signs)
        userturn = input("Rock(R) Paper(P) Scissors(S).. Your Turn : ")

        if(userturn in ['R','r','Rock']):
            userturn= 'Rock'
        elif(userturn in ['P', 'p', 'Paper']):
            userturn= 'Paper'
        elif(userturn in  ['S', 's', 'Scissors'] ):
            userturn= 'Scissors'

        print('CPU {' + CPUturn + '} VS YOU {' + userturn + '}')
        if(userturn == CPUturn):
            x=x-1
            print('')
        else:
            if(userturn in ['R','r','Rock'] and CPUturn == 'Scissors'):
                GameBoard[1][x] = 'X'
                GameBoard[2][x] = 'O'
                userwin += 1
            elif(userturn in ['R','r','Rock'] and CPUturn == 'Paper'):
                GameBoard[1][x] = 'O'
                GameBoard[2][x] = 'X'
                CPUwin += 1
            elif (userturn in ['P', 'p', 'Paper'] and CPUturn == 'Rock'):
                GameBoard[1][x] = 'X'
                GameBoard[2][x] = 'O'
                userwin += 1
            elif (userturn in ['P', 'p', 'Paper'] and CPUturn == 'Scissors'):
                GameBoard[1][x] = 'O'
                GameBoard[2][x] = 'X'
                CPUwin += 1
            elif (userturn in ['S', 's', 'Scissors'] and CPUturn == 'Paper'):
                GameBoard[1][x] = 'X'
                GameBoard[2][x] = 'O'
                userwin += 1
            elif (userturn in ['S', 's', 'Scissors'] and CPUturn == 'Rock'):
                GameBoard[1][x] = 'O'
                GameBoard[2][x] = 'X'
                CPUwin += 1

            print("Game Status:")
            print(makePrettyTable(user,GameBoard[0],GameBoard[1],GameBoard[2]))
            print('')
            if(userwin > 1):
                print("You WON!!!")
                break
            elif(CPUwin > 1):
                print("CPU WON!! Better Luck Next Time..")
                break
    print('')

    replay = input("Do you want to play the game again(y/n): ")
    if(replay not in ['s','Y','y','Yes','yes']):
        break