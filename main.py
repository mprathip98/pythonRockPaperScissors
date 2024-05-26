import random

results = ["r", "p", "s"]


score_player = 0
score_comp = 0

while True:
    user_play = input("First to 3 wins! Choose r for Rock, p for Paper, and s for Scissors. Or hit q to quit")

    if user_play == "q":
        print("That's alright!")
        quit()
    comp_play = results[random.randrange(0, 3)]

    if comp_play == user_play:
        print("Tie")

    if comp_play == "r" and user_play == "s":
        print("The computer chose rock and won")
        score_comp += 1
    if comp_play == "p" and user_play == "r":
        print("The computer chose paper and won")
        score_comp += 1
    if comp_play == "s" and user_play == "p":
        print("The computer chose scissor and won")
        score_comp += 1

    if comp_play == "s" and user_play == "r":
        print("The computer chose scissors")
        print("You won")
        score_player += 1
    if comp_play == "r" and user_play == "p":
        print("The computer chose rock")
        print("You won")
        score_player += 1
    if comp_play == "p" and user_play == "s":
        print("The computer chose paper")
        print("You won")
        score_player += 1
    if score_player == 3:
        print("CONGRATS! YOU WON!")
        quit()
    if score_comp == 3:
        print("WOMP WOMP! YOU LOST!")
        quit()