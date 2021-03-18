import random

def play():
    user = input("Please select your fighter: 'r' for 🥌 , 's' for ✂  and  'p' for 📜 \n")
    computer = random.choice(['r', 'p', 's'])

    if user == 'r':
        print("Your choice is:  🥌")
    elif user == 's':
        print ("Your choice is:  ✂")
    else:
        print ("Your choice is:  📜")

    if computer == 'r':
        print("Enemy's choice is:🥌")
    elif computer == 's':
        print("Enemy's choice is:✂")
    else:
        print("Enemy's choice is:📜")
    if user == computer:
        return "it's a draw! ⚖"

    if is_win(user, computer):
        return 'You won! 🥇'

    return "You lost! ☠"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True

print(play())
