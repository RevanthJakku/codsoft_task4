import random
def play_game():
    print("Welcome to Rock, Paper, Scissors")
    print('''Rules for playing the game
    > Rock beats Scissors
    > Paper beats Rock
    > Scissors beats Paper
    > Enter 1 for Rock, 2 for Paper, 3 for Scissors'''
          )
    user_choice = input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: ")
    if user_choice not in ["0", "1", "2"]:
        print("Invalid Choice. PLease enter 0, 1, or 2.")
        play_again = input("Do you want to play again? (Yes/No): ")
        if play_again.lower() == "yes":
            play_game()
        else:
            print("Good Bye")
            return


    user_choice = int(user_choice)
    computer_choice = random.randint(0,2)
    print("Computer Choice is: ", computer_choice)

    if user_choice <= 2 and computer_choice <= 2:
        if user_choice == 0 and computer_choice == 2:
            print("You Win")
        elif user_choice == 2 and computer_choice == 0:
            print("You Win")
        elif computer_choice > user_choice:
            print("You Lose")
        elif computer_choice < user_choice:
            print("You Win")
        elif computer_choice == user_choice:
            print("Draw")
    else:
        print("Invalid Choice")

    play_again = input("Do you want to play_again?(Yes/No): ")
    if play_again.lower() == "yes":
        play_game()
    else:
        print("Good Bye")

play_game()