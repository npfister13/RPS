import play_rps

print("Welcome to Rock, Paper, Scissors!")
game_length = int(input("How much would you like to play? Best of 3 or best of 5?\nPlease input 3 or 5 to choose.\n"
                    "Enter 0 to quit.\n>"))

opponent_score = 0
user_score = 0

while game_length != 0:
    while (user_score or opponent_score) != (game_length + 1)/2:
        winner = play_rps.game_time()
        if winner == "u":
            user_score += 1
        elif winner =="o":
            opponent_score+=1
        else:
            user_score+=0
            opponent_score+=0

    print("The winner is..." )
    if user_score > opponent_score:
        print("You! You won %s - %d." % (user_score, opponent_score))
    elif opponent_score > user_score:
        print("The opponent! They won %s - %d." % (opponent_score, user_score))
    else:
        print("It's a tie!")
    print("\n")
    game_length = int(input("If you want to continue playing, enter 3 for best of 3 or 5 for best of 5. "
                        "Otherwise, enter 0 to exit: "))
    user_score = 0
    opponent_score = 0
print("bye!")
