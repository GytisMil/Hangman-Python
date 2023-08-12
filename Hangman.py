#Main file to launch Hangman game
import Singleplayer_functions

print("Welcome to Hangman game made in Python.")
print("Play Singleplayer (S) or Multiplayer (M)?")
print("If you launched this file accidentally, then you can type 'Q' to quit.")
mode = input()
while(mode != "S" and mode != "s" and mode != "M" and mode != "m" and mode != "Q" and mode != "q"):
    print("Invalid input.")
    print("Play Singleplayer (S) or Multiplayer (M)?")
    print("If you launched this file accidentally, then you can type 'Q' to quit.")
    mode = input()
if(mode == "S" or mode == "s"):
    WordSeed = 0
    print("Singleplayer mode selected!")
    Singleplayer_functions.CreateWordArray()
    WordSeed = Singleplayer_functions.GenerateWord()
    print(WordSeed)
elif(mode == "M" or mode == "m"):
    print("Multiplayer mode selected!")