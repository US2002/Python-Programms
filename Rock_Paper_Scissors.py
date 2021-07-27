import random


def rules():
    print('''\nWinning Rules of the Rock paper scissor game as follows:
Rock vs paper->paper wins
Rock vs scissor->Rock wins
paper vs scissor->scissor wins\n''')


def user_input(player):
    if player == "1" or player == "rock":
        player = 'rock'
        computer_input(player)
    elif player == "2" or player == "paper":
        player = 'paper'
        computer_input(player)
    elif player == "3" or player == "scissors":
        player = 'scissors'
        computer_input(player)
    else:
        print("Invalid Choice!!!")


def computer_input(player):
    Player = player.lower()
    print(f"\nYou chose {Player}\n")
    print("Now computer is Choosing........")

    Choices = ["rock", "paper", "scissors"]
    Computer = random.choice(Choices)
    print(f"Computer chose {Computer}.\n")
    determine(Player, Computer)


def determine(Player, Computer):
    if Player == Computer:
        print(f"Both players selected {Player}. It's a tie!")
    elif Player == "rock":
        if Computer == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif Player == "paper":
        if Computer == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif Player == "scissors":
        if Computer == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")


rules()
while True:
    player = input('''Enter a choice
1.rock
2.paper
3.scissors
--->''')
    user_input(player)
    repeat = input("\nPlay again? (y/n): ")
    if repeat.lower() != "y" and repeat.lower() != "yes":
        break
print("\nTHANKS FOR PLAYING!!!!")
