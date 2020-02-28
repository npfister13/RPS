import random



class Score:
    def __init__(self):
        self.user_score = 0
        self.opponent_score = 0
        self.user_wins = 0
        self.opponent_wins = 0

def main():
    print("Welcome to Rock, Paper, Scissors!\nHow much would you like to play? ")
    print("Input any integer to play.\nEnter 0 to quit.")

    while True:
        try:
            game_length = int(input(">"))
            break
        except ValueError:
            print("Please enter any integer above 0 to play.")

    score = Score()
    user_score = score.user_score
    opponent_score = score.opponent_score
    user_wins = score.user_wins
    opponent_wins = score.opponent_wins

    while game_length != 0:
        while (user_score < game_length) and (opponent_score < game_length):
            winner = game_time()
            if winner == "u":
                user_score += 1
            elif winner == "o":
                opponent_score += 1
            else:
                pass

        print("The winner is...")
        if user_score > opponent_score:
            print("You! You won %s - %d." % (user_score, opponent_score))
            user_wins += 1
            print("Total sets you've won: %s" % user_wins)
            print("Total sets your opponent has won: %s" % opponent_wins)
        elif opponent_score > user_score:
            print("The opponent! You lost %s - %d." % (opponent_score, user_score))
            opponent_wins += 1
            print("Total sets you've won: %s" % user_wins)
            print("Total sets your opponent has won: %s" % opponent_wins)

        print("\n")
        print("If you want to continue playing, enter any integer. Otherwise, enter 0 to exit. ")
        user_score = 0
        opponent_score = 0



def user_choice():
    users_choice = input("r, p, or s: ")
    return users_choice


def opponent_choice():
    opponents_choice = random.choice(['r', 'p', 's'])
    return opponents_choice


def check_input(selection):
    if selection not in ['r','p','s']:
        print("Invalid input. Try again.")

    return selection


def game_time():
    users_choice = user_choice().lower()
    opponents_choice = opponent_choice()

    # check if valid input
    while users_choice not in ['r', 'p', 's']:
        print("Invalid input. Please try again.")
        users_choice = user_choice().lower()

    print("You:", users_choice)
    print("Opponent:", opponents_choice)

    if (users_choice == "r" and opponents_choice == "p") or (users_choice == "s" and opponents_choice == "r") or (
            users_choice == "p" and opponents_choice == "s"):
        print("Opponent wins!\n")
        return ("o")
    elif (users_choice == "r" and opponents_choice == "s") or (users_choice == "p" and opponents_choice == "r") or (
            users_choice == "s" and opponents_choice == "p"):
        print("You win!\n")
        return ("u")
    else:
        print("It's a tie!\n")
        return ("t")

main()

print("bye!")
