#Main file to launch Hangman game
import Singleplayer_functions
import Two_Player_functions
print("Welcome to Hangman game made in Python.")
print("Play Singleplayer (S) or Dual-Player (T)?")
print("If you launched this file accidentally, then you can type 'Q' to quit.")
mode = input()
while(mode != "S" and mode != "s" and mode != "t" and mode != "t" and mode != "Q" and mode != "q"):
    print("Invalid input.")
    print("Play Singleplayer (S) or Dual-Player (T)?")
    print("If you launched this file accidentally, then you can type 'Q' to quit.")
    mode = input()
if(mode == "S" or mode == "s"):
    print("Singleplayer mode selected!")
    WordList = Singleplayer_functions.CreateWordArray()
    SPagain = ''
    while(SPagain != "N" and SPagain != "n"):
        WordSeed = Singleplayer_functions.GenerateWordSeed()
        Word = Singleplayer_functions.GetNewWord(WordSeed, WordList)
        print("Word generated!")
        Correct_Letters = Singleplayer_functions.MakeWordLetters(Word)
        Singleplayer_functions.Singleplayer_game(Correct_Letters)
        print("Play again? (Y/N)")
        SPagain = input()
        while(SPagain != "N" and SPagain != 'n' and SPagain != 'Y' and SPagain != 'y'):
            print("Invalid input.")
            print("Play again? (Y/N)")
            SPagain = input()
elif(mode == "T" or mode == "t"):
    print("Dual-Player mode selected!")
    Hanger = 1
    Guesser = 2
    print("Do you need instructions how this game works? (Y/N)")
    instruct = input()
    while(instruct != "N" and instruct != 'n' and instruct != 'Y' and instruct != 'y'):
        print("Invalid input.")
        instruct = input()
    if(instruct == 'Y' or instruct == 'y'):
        Two_Player_functions.Instructions()