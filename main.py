import random


def GameWin(comp, you):
    if comp == you:
        return None
    elif comp == 'Rock':
        if you == 'Paper':
            return True
        elif you == 'Scissor':
            return False
    elif comp == 'Paper':
        if you == 'Scissor':
            return True
        elif you == 'Rock':
            return False
    elif comp == 'Scissor':
        if you == 'Rock':
            return True
        elif you == 'Paper':
            return False


print("Use Capital R for Rock, P for Paper, S for Scissor")
RNum = random.randint(1, 3)
if RNum == 1:
    comp = 'Rock'
elif RNum == 2:
    comp = 'Paper'
elif RNum == 3:
    comp = 'Scissor'

PTurn = input("Player Turn : Rock Paper Scissor ")
if PTurn == 'R':
    you = 'Rock'
elif PTurn == 'P':
    you = 'Paper'
elif PTurn == 'S':
    you = 'Scissor'

a = GameWin(comp, you)

print(f"Computer chose {comp}")
print(f"Player chose {you}")

if a == None:
    print("The game is tie")
elif a == True:
    print("The game is won")
elif a == False:
    print("The game is lost")