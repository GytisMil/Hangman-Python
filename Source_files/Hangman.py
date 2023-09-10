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
        Word_Letters = Singleplayer_functions.MakeWordLetters(Word)
        Singleplayer_functions.Singleplayer_game(Word_Letters)
        print("Play again? (Y/N)")
        SPagain = input()
        while(SPagain != "N" and SPagain != 'n' and SPagain != 'Y' and SPagain != 'y'):
            print("Invalid input.")
            print("Play again? (Y/N)")
            SPagain = input()
elif(mode == "T" or mode == "t"):
    print("Dual-Player mode selected!")
    Hanger = "Two"
    Guesser = "One"
    print("Do you need instructions how this game works? (Y/N)")
    instruct = input()
    while(instruct != "N" and instruct != 'n' and instruct != 'Y' and instruct != 'y'):
        print("Invalid input.")
        instruct = input()
    if(instruct == 'Y' or instruct == 'y'):
        Two_Player_functions.Instructions()
    DPagain = ''
    while(DPagain != 'n' and DPagain != 'N'):
        Hanger, Guesser = Two_Player_functions.ChangeRoles(Hanger, Guesser)
        Two_Player_functions.DisplayCurrentRoles(Hanger, Guesser)
        Confirmed_word = ''
        while(Confirmed_word != 'Y' and Confirmed_word != 'y'):
            Word = Two_Player_functions.WriteWord()
            Word_Letters = Two_Player_functions.MakeWordLetters(Word)
            Confirmed_word = Two_Player_functions.DisplayChoice(Word_Letters)
        print("Starting game...")
        #Two_Player_functions.HideWord()
        Two_Player_functions.Multiplayer_game(Word_Letters)
        print("Play again? (Y/N)")
        DPagain = input()
        while(DPagain != "N" and DPagain != 'n' and DPagain != 'Y' and DPagain != 'y'):
            print("Invalid input.")
            print("Play again? (Y/N)")
            DPagain = input()
        