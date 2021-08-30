import random

# Function to evaluate the winner of the game
def game_win(computer, user):
    if computer == user:
        return None
    elif computer == "Rock":
        if user == "Paper":
            return True
        return False
    elif computer == "Paper":
        if user == "Scissor":
            return True
        return False
    elif computer == "Scissor":
        if user == "Rock":
            return True
        return False


# Determining the computer choice
print("Use Capital R for Rock, P for Paper, S for Scissor")
randum_number = random.randint(1, 3)
if randum_number == 1:
    computer = "Rock"
elif randum_number == 2:
    computer = "Paper"
elif randum_number == 3:
    computer = "Scissor"

# Selection of the user choice
player_turn = input("Player Turn : Rock Paper Scissor? ")
if player_turn == "R":
    user = "Rock"
elif player_turn == "P":
    user = "Paper"
elif player_turn == "S":
    user = "Scissor"

# Calling the evaluation function
result = game_win(computer, user)

# Priting the results
print(f"Computer chose {computer}")
print(f"Player chose {user}")
if result is None:
    print("The game is a tie")
elif result is True:
    print("The game is won")
elif result is False:
    print("The game is lost")
