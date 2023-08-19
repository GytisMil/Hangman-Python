from datetime import datetime
import random
import os
def CreateWordArray():
    wlist = open("English_dictionary.txt", "r")
    words = [0] * 370102
    counter = 0
    for x in wlist:
        words[counter] = x
        counter += 1
    random.shuffle(words)
    return words
        
def GenerateWordSeed():
    print("Generating a word...")
    seed = int(datetime.utcnow().timestamp()) % 370102
    return seed

def GetNewWord(seed, wlist):
    os.system('cls')
    return wlist[seed]

def MakeWordLetters(word):
    letters = [0] * len(word)
    counter = 0
    for letter in word:
        letters[counter] = word[counter]
        counter += 1
    letters.pop(len(letters) - 1)
    letters[0] = letters[0].upper()
    return letters

def CheckRepeater(letter, guesslist, guesscounter):
    if letter.lower() in guesslist and letter.upper() in guesslist:
        guesslist[guesscounter] = 0
    else:
        guesslist[guesscounter] = letter
        guesscounter += 1

def CheckGuess(lives, letter, word):
    if letter.lower() not in word and letter.upper() not in word:
        lives -= 1
        return lives
    else:
        return lives

def PrintCurrentLetters(letters, guesses):
    for letter in letters:
        if letter.lower() in guesses or letter.upper() in guesses:
            if(letter != letters[len(letters) - 1]):
                print(letter + " ", end = "")
            else:
                print(letter)
        else:
            if(letter != letters[len(letters) - 1]):
                print("_ ", end = "")
            else:
                print("_")

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

def Singleplayer_game(word, letters):
    lives = 5
    guesses = [0] * (lives * len(letters))
    guesscount = 0
    currentword = letters
    while(lives > 0):
        print(currentword)
        print("You currently have " + str(lives) + " lives.")
        PrintCurrentLetters(currentword, guesses)
        if(guesscount != 0):
            PrintUsedLetters(guesses, guesscount)
            guess = input("Guess the letter:")
            if(guess.strip() != '' and len(guess) == 1):
                CheckRepeater(guess, guesses, guesscount)
                lives = CheckGuess(lives, guess, letters)
                #os.system('cls')
            else:
                #os.system('cls')
                print("Invalid input. Try again.")
        else:
            guess = input("Guess the letter:")
            if(guess.strip() != '' and len(guess) == 1):
                guesses[guesscount] = guess
                guesscount += 1
                lives = CheckGuess(lives, guess, letters)
                #os.system('cls')
            else:
                #os.system('cls')
                print("Invalid input. Try again.")
