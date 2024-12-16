import random

def game():
    print("Winning rules of the game ROCK PAPER SCISSORS are:")
    print(" Rock vs Paper -> Paper wins\n","Rock vs Scissors -> Rock wins\n","Paper vs Scissors -> Scissors wins" )

    print("Options:")

    print(" 1 - Rock\n", "2 - Paper\n", "3 - Scissors")

    x = int(input("Enter your choice: "))

    if x == 1:
        choice = "Rock"
    elif x == 2:
        choice = "Paper"
    elif x == 3:
        choice = "Scissors"
    #elif x != 1 or x != 2 or x != 3:
    elif x not in [1,2,3]:
        print("Invalid choice")
        exit()

    print("Your choice is", choice)

    print("Now it's computers turn...")

    comp = random.randint(1,3)

    if comp == 1:
        comp_choice = "Rock"
    elif comp == 2:
        comp_choice = "Paper"
    elif comp == 3:
        comp_choice = "Scissors"

    print("Computer choice is", comp_choice)
    print(choice,"vs", comp_choice)


    if comp_choice == choice:
       print("It's a tie!")
    elif choice == "Rock" and comp_choice == "Scissors":
        print("You win!")
    elif choice == "Rock" and comp_choice == "Paper":
        print("You lose!")
    elif choice == "Paper" and comp_choice == "Scissors":
        print("You lose!")
    elif choice == "Paper" and comp_choice == "Rock":
        print("You win!")
    elif choice == "Scissors" and comp_choice == "Paper":
        print("You win!")
    elif choice == "Scissors" and comp_choice == "Rock":
        print("You lose!")




def game_end():
    print("Want to play again? (Y/N)")
    answer = str.lower(input())
    if answer == "n":
        print("Thank you for playing!")
        exit()
    elif answer == "y":
        game()
        game_end()
    else:
        print("Invalid input")

game()
game_end()







