import random

name = input("Enter Your Name: ")
HangmanWord = ['spiderman', 'superman']
Game = True
global GameWord


def GuessWord(guesses):
    GuessedWord = ''
    for x in GameWord:
        if x in guesses:
            GuessedWord += x + " "
        else:
            GuessedWord += "_ "

    if (GuessedWord.replace(' ','') == GameWord):
        return True
    else:
        print("Find out this SuperHero Name : " + GuessedWord)
        return False


def drawHangman(attempt):
    print("______________")
    print("     |     ")
    if (attempt > 0):
        print("     O     ")
    if(attempt == 1):
        print("     |     ")
    if (attempt == 2):
        print("   / |     ")
    if (attempt >= 3):
        print("   / | \   ")
    if (attempt == 4):
        print("    /      ")
    if (attempt >= 5):
        print("    / \    ")

print("Hey "+name.capitalize()+", Let's test your guessing skills in HANGMAN...")
while True:
    attempt = 0
    GameWord = random.choice(HangmanWord)
    guesses = []
    GuessedWord = ''

    while Game:
        print("")
        Won = GuessWord(guesses)

        if Won:
            print("Congratulations! You WON !!!")
            Game = False
            break

        letter = input("Enter Your Guess: ").strip().lower()

        if(letter in GameWord and letter not in guesses and len(letter) == 1):
            guesses.append(letter)
        else:
            if(attempt>5):
                print("")
                print(" GAME OVER..! Sorry Try Later...")
                Game = False
                break
            if (len(letter) != 1):
                print("Invalid Letter")

            if letter in guesses:
                print("Letter already Guessed..")
            drawHangman(attempt)
            attempt = attempt+1

    print('')
    replay = input("Do you want to play again (y/n) : ")
    if replay in ['n', 'N', 'No']:
        break
    elif replay in ['y', 'Y', 'Yes']:
        Game = True

