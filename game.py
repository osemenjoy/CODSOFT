import random

comp_score = 0
guest_score = 0
guest = input("Enter you name: ")
while True:
    comp_choices = ["rock", "paper", "scissors"]
    guest_choice = input("Enter choice (rock, paper or scissors): ")
    random.shuffle(comp_choices)

    for i in comp_choices:
        comp_choice = i
        print(f"Computer choice: {comp_choice}")
        break

    if comp_choice == guest_choice:
        print("It's a tie")
    elif comp_choice == "paper" and guest_choice == "scissors":
        guest_score += 1
        print(f"Your score: {guest_score}")
    elif comp_choice == "rock" and guest_choice == "paper":
        guest_score += 1
        print(f"Your score: {guest_score}")
    elif comp_choice == "scissors" and guest_choice == "rock":
        guest_score += 1
        print(f"Your score: {guest_score}")
    else:
        comp_score += 1
        print(f'computer score is {comp_score}')
    end_game = input("Do you want to end game(y/n): ")
    if end_game == "y":
        print(f"Your score is {guest_score}")
        print(f"Computer score is {comp_score}")
        if guest_score > comp_score:
            print("You win.")
        else:
            print("sorry, you lose.")
        break