import random

rock = 0
paper = 1
scissors = 2

total = [rock,paper,scissors]
ran_num = random.randint(0,2)

player_choice = int(input("What do you choose? type 0 for rock, 1 paper and 2 scissors. "))
computer_choice = total[ran_num]

if computer_choice == rock and player_choice == scissors:
    print("Rock beats scissors")
    print("Computer wins!")
elif computer_choice == scissors and player_choice == rock:
    print("Rock beats scissors")
    print("You win!")
elif computer_choice == scissors and player_choice == paper:
    print("Scissors beats paper")
    print("Computer wins!")
elif computer_choice == paper and player_choice == scissors:
    print("Scissors beats paper.")
    print("You win!")
elif computer_choice == paper and player_choice == rock:
    print("Paper beats rock")
    print("Computer wins!")
elif computer_choice == rock and player_choice == paper:
    print("Paper beats rock.")
    print("You win!")
elif computer_choice == player_choice:
    print("Draw!")
else:
    print("I don`t understand, please try again!")