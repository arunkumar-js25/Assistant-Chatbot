def intro():
    global name
    name = input("Enter Player Name: ")
    print("""
    Hi """+ name +""" from Fairy Tail guild,  """)

def Rooms():
    print("""    -------------
    | 1 | 2 | 3 |
    -------------
    | 4 | 5 | 6 |
    -------------
    | 7 | 8 | X |
    -------------    """)

def RoomA():
    if (len(tracker) >= 'RoomA'):
        tracker += ' --> RoomA'

def RoomB():
    tracker += ' --> RoomA'

def RoomC():
    print()

def RoomD():
    print("4")

def RoomE():
    print()

def RoomF():
    print()

def RoomG():
    print()

def RoomH():
    print()

def RoomI():
    print()

def Choice(func):
    GameRoom[func]()

global tracker
tracker = 'RoomA'
GameRoom = {'RoomA':RoomA,'RoomB':RoomB,
            'RoomC':RoomC,'RoomD': RoomD,
            'RoomE':RoomE,'RoomC':RoomF,
             'RoomG': RoomG,'RoomH':RoomH}

intro()
Rooms()
if input("Shall we start the game: (Y/N)") not in ['n', 'N', 'No']:
    while True:
        print("Restart(r) Quit(q) LiveMap(l)")
        print("Restart(r) Quit(q) LiveMap(l)")
        move = input()
        if move == 'l':
            print('Live Location: ' + tracker.split(' --> ')[-1])
            print('Track: ' + tracker)
        elif move == 'q':
            break
        elif move == 'r':
            print('******************************')
            print('')


