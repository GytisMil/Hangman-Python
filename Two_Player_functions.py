import re
def Instructions():
    print("There are two players: Hanger and Guesser.\nFirst player, the Hanger, will write the word, where second player, the Guesser, has to figure it out.")
    print("Important to note - the word cannot have any numbers (obviously) and no special symbols (ex. ice-cream is not allowed, but ice cream is.)")
    print("The Guesser has 5 lives to find out what Hanger wrote.\nThe round ends when Guesser figures the word out or rans out of lives.")
    print("Keep in mind, after every round - the roles of players switches.\nYou can end Hangman game at the end of the round, when prompt to continue appears.")

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
            print("Too many spaces. You're writing a word, not a paragraph.")
            return False
    else:
        print("Invalid input. Try again.")
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