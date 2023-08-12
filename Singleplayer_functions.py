from datetime import datetime
import random
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
    return wlist[seed]