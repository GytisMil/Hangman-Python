from datetime import datetime

def CreateWordArray():
    wlist = open("English_dictionary.txt", "r")
    words = [0] * 370102
    counter = 0
    for x in wlist:
        words[counter] = x
        counter += 1
        

def GenerateWord():
    print("Generating a word...")
    seed = int(datetime.utcnow().timestamp()) % 370102
    return seed
