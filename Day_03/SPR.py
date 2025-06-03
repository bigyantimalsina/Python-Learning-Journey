import random

options = ("rock", "paper", "scissor")
playing = True

while playing:
    player = None 
    name = input("Enter your name: ")

    while player not in options:
        player = input("Enter your choice (rock, paper, scissor): ").lower()

    computer = random.choice(options)  

    print(f"Player = {player}")
    print(f"Computer = {computer}")

    if player == computer:
        print("It's a tie")
    elif (player == "paper" and computer == "rock") or \
         (player == "rock" and computer == "scissor") or \
         (player == "scissor" and computer == "paper"):
        print(f"{name} wins!")
    else:
        print(f"{name} loses!")

    if input("Play again? (y/n): ").lower() != "y":
        playing = False

print("Thanks for playing!")
