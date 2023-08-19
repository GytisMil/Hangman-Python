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
    print("Singleplayer mode selected!")
    WordSeed = Singleplayer_functions.GenerateWordSeed()
    WordList = Singleplayer_functions.CreateWordArray()
    Word = Singleplayer_functions.GetNewWord(WordSeed, WordList)
    print("Word generated!")
    Correct_Letters = Singleplayer_functions.MakeWordLetters(Word)
    Singleplayer_functions.Singleplayer_game(Word, Correct_Letters)
elif(mode == "M" or mode == "m"):
    print("Multiplayer mode selected!")