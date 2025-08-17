import random
from enum import Enum
import  sys
def rps_start():
    Plscore = 0
    Cpscore = 0
    Gameplayed = 0
    def play_rps():
        class RPS(Enum):
            ROCK = 1
            SCISSOR = 2
            PAPER = 3
        Player_name = input("\nEnter your name: ")
        Player = input("\n1 for Rock\n2 for scissors\n3 for Paper\nChoose:")
        PlayerChoice = int(Player)

        if PlayerChoice not in [1,2,3]:
            print(" Select between 1-3 ")
            return play_rps()

        computer = random.choice("123")
        ComputerChoice = int(computer)

        print(f"\n{Player_name} choose {str(RPS(PlayerChoice)).replace('RPS.','')}")
        print(f"\nComputer choose {str(RPS(ComputerChoice)).replace('RPS.','')}")
        nonlocal Plscore
        nonlocal Cpscore
        nonlocal Gameplayed
        
        if PlayerChoice == 1 and ComputerChoice == 2:
            print(f"\n-----😁 {Player_name} Win----")
            Plscore += 1
        elif PlayerChoice == 2 and ComputerChoice == 3:
            print(f"\n-----😁 {Player_name} Win----")
            Plscore += 1
        elif PlayerChoice == 3 and ComputerChoice == 1:
            print(f"\n-----😁 {Player_name} Win----")
            Plscore += 1
        elif PlayerChoice ==  ComputerChoice :
            print("\n-----❤ TIE----")
        else:
            print(f"\n---🤷 Computer Won--- {Player_name} wanna try again ?")
            Cpscore += 1
            
        Gameplayed += 1
        print(f"\nTotal Games Played = {Gameplayed}")
        print(f"\n{Player_name} Score = {Plscore}.")
        print(f"Computer Score = {Cpscore}.")

        while True:
            Playagain = input("\n Press Y for Play again and press Q for Exit:\n")
            if Playagain.lower() not in ["y","q"]:
                continue
            else:
                break
        if Playagain.lower() == "y":
            return play_rps()
        else:
            print("\n✌ Thnks for playing")
            sys.exit(f"\n-----👋 bye.....bye {Player_name}----")

    play_rps()
rps_start()