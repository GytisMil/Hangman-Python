import re
import os
def Instructions():
    print("There are two players: Hanger and Guesser.\nFirst player, the Hanger, will write the word, where second player, the Guesser, has to figure it out.")
    print("Important to note - the word cannot have any numbers (obviously) and no special symbols (ex. ice-cream is not allowed, but ice cream is.)")
    print("The Guesser has 5 lives to find out what Hanger wrote.\nThe round ends when Guesser figures the word out or rans out of lives.")
    print("Keep in mind, after every round - the roles of players switches.\nYou can end Hangman game at the end of the round, when prompt to continue appears.")
    print("Lastly, the game is running on Honor system - Guesser has to look away when Hanger is writing it's word! Don't cheat!")

def ChangeRoles(Hanger, Guesser):
    c = Hanger
    Hanger = Guesser
    Guesser = c
    return Hanger, Guesser

def DisplayCurrentRoles(Hanger, Guesser):
    print("Current roles:\nHanger - Player " + Hanger + "\nGuesser - Player " + Guesser)

def HideWord(): #Anti-Cheat measure
    counter = 0
    while(counter < 20000):
        print("")
        counter += 1
def WriteWord():
    print("Write your word: ", end = "")
    word = input()
    Passable = CheckWord(word)
    while(Passable==False):
        word = input()
        Passable = CheckWord(word)
    return word

def CheckWord(word):
    if(bool(re.search('^[a-zA-Z ]*$',word))==True):
        Spacecount = word.split()
        if(len(Spacecount) < 3):
            return True
        else:
            print("Too many spaces. You're writing a word, not a paragraph.\nWrite your word: ", end="")
            return False
    else:
        print("Invalid input. Try again.\n Write your word: ", end="")
        return False
    
def MakeWordLetters(word):
    Newword = word.split() #Used to remove all spaces
    First_letters = [0] * len(Newword[0])
    counter = 0
    for letter in Newword[0]:
        First_letters[counter] = letter
        counter += 1
    First_letters[0] = First_letters[0].upper()
    Final_letters = First_letters
    if(len(Newword) == 2):
        Second_letters = [0] * len(Newword[1])
        counter = 0
        for letter in Newword[1]:
            Second_letters[counter] = letter
            counter += 1
        Final_letters.append(" ")
        Final_letters += Second_letters
        return Final_letters
    else:
        return Final_letters

def DisplayChoice(letters):
    print("Your word is:", end="")
    choosen_word = CreateFullWord(letters)
    print("'" + choosen_word + "'.")
    print("Do you accept? (Y/N)")
    confirm = input()
    while(confirm != "N" and confirm != 'n' and confirm != 'Y' and confirm != 'y'):
        print("Invalid input.")
        confirm = input()
    return confirm

def CreateFullWord(letters):
    word = ''
    for letter in letters:
        word += letter
    return word

def HangerWin(letters):
    print("Hanger Won!")
    answer = CreateFullWord(letters)
    print("The answer was '" + answer + "'")

def GuesserWin(letters, lives):
    print("Guesser Won!")
    answer = CreateFullWord(letters)
    print("Hanger's word was '" + answer + "'")
    print("Guesser had " + str(lives) + " lives remaining.")

#Reusing functions made in Singleplayer
def Multiplayer_game(letters):
    os.system('cls')
    lives = 5
    guesses = [0] * (lives * len(letters))
    guesscount = 0
    revealed = False
    currentword = letters
    while(lives > 0 and revealed == False):
        print("Guesser currently has " + str(lives) + " lives.")
        PrintCurrentLetters(currentword, guesses)
        if(guesscount != 0):
            PrintUsedLetters(guesses, guesscount)
            guess = input("Guess the letter:")
            if(guess.strip() != '' and len(guess) == 1 and bool(re.search('^[a-zA-Z]*$',guess)) == True):
                if(CheckRepeater(guess, guesses, guesscount)):
                    guesscount += 1
                    lives = CheckGuess(lives, guess, letters)
                    revealed = CheckReveal(letters, guesses)
                    os.system('cls')
                else:
                    os.system('cls')
                    print("You already used this letter!")
            else:
                os.system('cls')
                print("Invalid input. Try again.")
        else:
            guess = input("Guess the letter:")
            if(guess.strip() != '' and len(guess) == 1 and bool(re.search('^[a-zA-Z]*$',guess))==True):
                guesses[guesscount] = guess
                guesscount += 1
                lives = CheckGuess(lives, guess, letters)
                os.system('cls')
            else:
                os.system('cls')
                print("Invalid input. Try again.")
    if(lives == 0):
        HangerWin(currentword)
    else:
        GuesserWin(currentword, lives)
        PrintUsedLetters(guesses, guesscount)

def PrintCurrentLetters(letters, guesses):
    for letter in letters:
        if letter.lower() in guesses or letter.upper() in guesses or letter == ' ':
            if(letter != letters[len(letters) - 1]):
                print(letter + " ", end = "")
            else:
                print(letter)
        else:
            if(letter != letters[len(letters) - 1]):
                print("_ ", end = "")
            else:
                print("_")

def CheckGuess(lives, letter, word):
    if letter.lower() not in word and letter.upper() not in word:
        lives -= 1
        return lives
    else:
        return lives

def CheckReveal(word, guesses):
    counter = 0
    for letter in word:
        if letter.lower() in guesses or letter.upper() in guesses or letter == " ":
            counter += 1
    if counter == len(word):
        return True
    else:
        return False
    
def PrintUsedLetters(guesses, counter):
    print("Used letters: ", end = "")
    x = 0
    while x < counter:
        if(x + 1 != counter):
            print(guesses[x] + " ", end="")
            x += 1
        else:
            print(guesses[x])
            x += 1

def CheckRepeater(letter, guesslist, guesscounter):
    if letter.lower() in guesslist or letter.upper() in guesslist:
        guesslist[guesscounter] = 0
        return False
    else:
        guesslist[guesscounter] = letter
        return True