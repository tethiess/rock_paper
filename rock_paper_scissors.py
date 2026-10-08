#Daniel Thiess
#IS303
#Assignment 5
# - Make a function that asks for a choice and makes it lowercase.
#   Keep asking until the choice is rock, paper, or scissors.
# - Make another function that compares choices and returns win, loss, or tie.
# - Welcome the player and ask how many rounds they want to play.
#   Keep asking until they give a positive odd whole number.
# - Start everyone's wins and losses at zero, along with the round count.
# - Keep playing until enough rounds are finished:
#   Get the player's choice, then pick a random choice for the computer.
#   Show the computer's choice and check who won.
#   If it's a tie, play again without counting that round.
#   Otherwise, update the wins and losses and count the round.
# - Show the final scores, announce the winner, and say thanks.

# - Random lets the computer pick a choice.
import random


def get_player_choice():
    # - Clean up extra spaces and capital letters.
    choice = input("Enter rock, paper, scissors: ").strip().lower()

    # - Ask again if the choice isn't one of these three.
    while choice not in ["rock", "paper", "scissors"]:
        print(f"Sorry, '{choice}' is not a valid choice. Please try again.")
        choice = input("Enter rock, paper, scissors: ").strip().lower()

    return choice


def determine_winner(player_choice, computer_choice):
    # - Matching choices mean nobody wins this round.
    if player_choice == computer_choice:
        return "tie"

    # - These are the three ways the player can win.
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "win"
    else:
        # - Anything else means the computer won.
        return "loss"


def main():
    # - Say hi and find out how many rounds to play.
    print(f"Welcome to Rock Paper Scissors!")

    while True:
        try:
            rounds = int(input("How many rounds would you like to play: "))
            # - The number needs to be positive and odd.
            if rounds > 0 and rounds % 2 == 1:
                break
            print(f"Sorry, the number must be a positive odd number. Please try again.")
        except ValueError:
            # - This catches things like words or decimals.
            print(f"Sorry, please enter a whole number.")

    # - Start all the scores and the round count at zero.
    player_wins = 0
    player_losses = 0
    computer_wins = 0
    computer_losses = 0
    rounds_played = 0

    while rounds_played < rounds:
        # - Get both choices and show what the computer picked.
        print(f"")
        player_choice = get_player_choice()
        computer_choice = random.choice(["rock", "paper", "scissors"])
        print(f"The computer chose {computer_choice}.")

        result = determine_winner(player_choice, computer_choice)

        if result == "tie":
            # - Ties don't change the scores or the round count.
            print(f"Tie! Play again.")
        elif result == "win":
            # - Give the player a win and the computer a loss.
            print(f"You won!")
            player_wins += 1
            computer_losses += 1
            rounds_played += 1
        else:
            # - Give the computer a win and the player a loss.
            print(f"You lost!")
            player_losses += 1
            computer_wins += 1
            rounds_played += 1

    # - Show how everyone did after all the rounds.
    print(f"")
    print(f"-------------------------------------------")
    print(f"Score - You: {player_wins} | Computer: {computer_wins}")
    print(f"Your wins: {player_wins} | Your losses: {player_losses}")
    print(f"Computer wins: {computer_wins} | Computer losses: {computer_losses}")

    # - Whoever has more wins takes the game.
    if player_wins > computer_wins:
        print(f"You win!!!")
    else:
        print(f"The computer wins!")

    print(f"Thanks for playing!")


# - Start the game when this file is run.
if __name__ == "__main__":
    main()
