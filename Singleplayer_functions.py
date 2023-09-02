from datetime import datetime
import random
import os
import re
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
    if letter.lower() in guesslist or letter.upper() in guesslist:
        guesslist[guesscounter] = 0
        return False
    else:
        guesslist[guesscounter] = letter
        return True

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

def CheckReveal(word, guesses):
    counter = 0
    for letter in word:
        if letter.lower() in guesses or letter.upper() in guesses:
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

def CreateFullWord(letters):
    word = ''
    for letter in letters:
        word += letter
    return word

def LossDisplay(letters):
    print("You lost!")
    answer = CreateFullWord(letters)
    print("The word was '" + answer + "'")

def WinDisplay(letters, lives):
    print("You won!")
    answer = CreateFullWord(letters)
    print("The word was '" + answer + "'")
    print("You had " + str(lives) + " lives remaining")

def Singleplayer_game(letters):
    lives = 5
    guesses = [0] * (lives * len(letters))
    guesscount = 0
    revealed = False
    currentword = letters
    while(lives > 0 and revealed == False):
        print("You currently have " + str(lives) + " lives.")
        PrintCurrentLetters(currentword, guesses)
        print(currentword)
        if(guesscount != 0):
            PrintUsedLetters(guesses, guesscount)
            guess = input("Guess the letter:")
            if(guess.strip() != '' and len(guess) == 1 and bool(re.search('^[a-zA-Z0-9]*$',guess)) == True):
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
            if(guess.strip() != '' and len(guess) == 1 and bool(re.search('^[a-zA-Z0-9]*$',guess))==True):
                guesses[guesscount] = guess
                guesscount += 1
                lives = CheckGuess(lives, guess, letters)
                os.system('cls')
            else:
                os.system('cls')
                print("Invalid input. Try again.")
    if(lives == 0):
        LossDisplay(currentword)
    else:
        WinDisplay(currentword, lives)
        PrintUsedLetters(guesses, guesscount)
