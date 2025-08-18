import random
import argparse
import sys
agspass = argparse.ArgumentParser()
agspass.add_argument("-n","-name",default="Unknown Player",help="Enter you name here")
agspasses = agspass.parse_args()
ags_name = agspasses.n

User_points = 0
Computer_points = 0 

def play_again():
    choice = input("\nWant to play again\nY for play and Q to quit :\n")
    if choice.lower() == "y":
        return choose()
    elif choice.lower() == "q":
        sys.exit(f"\n🤞Bye.....bye..{ags_name}")
    else:
        print("Press Y or Q")
        return play_again()

def st_game(user,computer):
    global User_points
    global Computer_points
    print(f"\n{ags_name} choose: {user}")
    print(f"Computer choose: {computer}\n")
    if user == computer:
        print(f"{ags_name}   Won\n{ags_name}  guessed it correctly")
        User_points += 1
        print(f"Total points of {ags_name}:{User_points}")
        print(f"Total points of Computer:{Computer_points}")
        play_again()
    else:
        print(f"Computer wins\n{ags_name}  failed to guess correctly")
        Computer_points += 1
        print(f"Total points of {ags_name}:{User_points}")
        print(f"Total points of Computer:{Computer_points}")
        play_again()

def choose():
    print(f"Hi {ags_name} !")
    user = input(f"\n{ags_name} please,enter a number between 1-3 :")
    users = int(user)
    if int(users) not in [1,2,3]:
        print("only number allowed between 1-9")
        choose()
    else:
        computer = str(random.choice("123"))
        print("")
        computers = int(computer)
        st_game(users,computers)


choose()
