"""
oponent: A for Rock, B for Paper, and C for Scissors
me in response: X for Rock, Y for Paper, and Z for Scissors
score: 1 for Rock, 2 for Paper, and 3 for Scissors
score: 0 if you lost, 3 if the round was a draw, and 6 if you won
"""
with open("2.txt", "r") as f:
    set = f.readlines()

list1 = [x.replace("\n", "") for x in set]
list2 = [x.split(" ") for x in list1]

X_score = 1
Y_score = 2
Z_score = 3

lose = 0
draw = 3
win = 6

total_score = 0

def game(user1, user2, score):
    if user1 == "A": # rock
        if user2 == "X":
            score = X_score + draw
        if user2 == "Y":
            score = Y_score + win
        if user2 == "Z":
            score = Z_score + lose
    elif user1 == "B": # paper
        if user2 == "X":
            score = X_score + lose
        if user2 == "Y":
            score = Y_score + draw
        if user2 == "Z":
            score = Z_score + win
    elif user1 == "C": # scissors
        if user2 == "X":
            score = X_score + win
        if user2 == "Y":
            score = Y_score + lose
        if user2 == "Z":
            score = Z_score + draw
    return score

for x in list2:
    user1 = x[0]
    user2 = x[1]
    a = game(user1, user2, total_score)
    total_score += a
    print(f"Score for this round: {a} and total score: {total_score}")

print(f"The game ended with total score: {total_score}")
