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
        if(bool(re.search(' {2,}',word))==False): #TODO Find more than two spaces
            Spacecount = word.split()
            if(len(Spacecount) <= 2):
                return True
            else:
                print("Too many spaces. You're writing a word, not a paragraph.")
                return False
        else:
            print("Invalid input. Check if you added multiple spaces.")
            return False
    else:
        print("Invalid input. Try again.")
        return False