from art import logo, vs
from data import data_game
import random

print(logo)
print("In this game, you need to guess who has more followers on Instagram :)")
score = 0

data_new_game = []
for x in data_game:
    data_new_game.append(x)

slot1 = " "
slot2 = " "
GAME = True

while GAME:
    if slot1 == " ":
        slot1 = random.choice(data_new_game)
    if slot2 == " ":
        slot2 = random.choice(data_new_game)

    while slot2 == slot1:
        slot2 = random.choice(data_new_game)

    if slot1['follower_count'] > slot2['follower_count']:
        winner = slot1
    else:
        winner = slot2

    print(f"You're score {score}")
    print(f"{slot1['description']} '{slot1['name']}' from {slot1['country']}")
    print(vs)
    print(f"{slot2['description']} '{slot2['name']}' from {slot2['country']}")
    while True:
        choose = input("Your reply? 1 or 2 ")
        try:
            choose = int(choose)
            if choose == 1 or choose == 2:
                break
            else:
                print("Unknown command!")
        except:
            print("Unknown command!")

    if choose == 1 and winner == slot1 or choose == 2 and winner == slot2:
        print("Perfect. This is the correct answer.")
        print(f"-"*40)
        score+=1

        if choose == 1:
            slot2_ind = data_new_game.index(slot2)
            data_new_game.pop(slot2_ind)
            slot2 = " "
        elif choose == 2:
            slot1_ind = data_new_game.index(slot1)
            data_new_game.pop(slot1_ind)
            slot1 = slot2
            slot2 = " "

    else:
        print(f"What a pity. This is the wrong answer. You lost.\nYoure score {score}")
        GAME = False

    if len(data_new_game) == 1:
        print(f"Game over. You won. Congratulations :) Youre score {score}")
        GAME = False

    if GAME == False:
        while True:
            new_game = input("Do you want to play again? 'y' or 'n' ").lower()
            if new_game == 'y':
                print(logo)
                print("In this game, you need to guess who has more followers on Instagram :)")
                score = 0
                data_new_game = []
                for x in data_game:
                    data_new_game.append(x)
                slot1 = " "
                GAME = True
                break
            elif new_game == 'n':
                print("Bye Bye. See you later.")
                break
