import random
import subprocess  # Module for running system commands safely
import sys         # Module for system-specific parameters and functions

def clear_screen():
    subprocess.run('cls' if sys.platform == 'win32' else 'clear', shell=True)


print("\n_____________________WELCOME TO THE GAME______________________\n")
i = 0
j = 1
user_win = 0
comp_win = 0
print("""Choose an option to play the game: 
Either choose the designated number or Write your pick.
    1. Rock
    2. Paper
    3.Scissor""")
while(i < 3):
    print(f"\n*****Round {j}*****\n")
    user_choice = input("Enter your choice: ")
    if user_choice in ['1','2','3']:
        i += 1
        j += 1
        choice = ["1", "2", "3"]
        comp_choice = random.choice(choice)
        if((user_choice == '1' and comp_choice == '2') or (user_choice == '2' and comp_choice == '3') or (user_choice == '3' and comp_choice == '1')):
            print(f"""YOU Selected: {user_choice}
COMPUTER Selected: {comp_choice}""")
            print("Computer Wins!!!\n")
            comp_win += 1
        elif(user_choice == comp_choice):
            print(f"""YOU Selected: {user_choice}
COMPUTER Selected: {comp_choice}""")
            print("The match is tie, You both get 1 point\n")
            comp_win += 1
            user_win += 1
        else:
            print(f"""YOU Selected: {user_choice}
COMPUTER Selected: {comp_choice}""")
            print("User Wins!!!\n")
            user_win += 1
    else:
        print("Error!!! Rerun the program and Select from the given option")
        i -= 1
        input("Enter any key to continue")
        clear_screen()
        continue
if(user_win < comp_win):
    print(f"Comp Wins The Game With Total Point: {comp_win}")
elif(user_win == comp_win):
    print("The match is a tie.")
else:
    print(f"User Wins The Game With Total Point: {user_win}")


