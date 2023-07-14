import random

RANDOM_NUMBER = random.randint(1,100)
PLAYER_HEARTS = 0

print("Welcome to the guess game!")
print(f"I'm guessing of a number between 1 and 100.")

difficulty_level = input("Choose a difficulty: 'Easy' or 'Hard'\n").lower()

if difficulty_level == "easy":
    PLAYER_HEARTS = 10
elif difficulty_level == "hard":
    PLAYER_HEARTS = 5

game_is_won = False


while not game_is_won:
    print(f"You have {PLAYER_HEARTS} attempts remaining to guess the number.")
    guess = int(input("Guess the number: "))
    if PLAYER_HEARTS == 1:
        print("You lose!")
        print(f'The number is {RANDOM_NUMBER}.')
        break
    if guess == RANDOM_NUMBER:
        print(f"You win!\nThe number is {RANDOM_NUMBER}.")
        game_is_won = True
    elif guess > RANDOM_NUMBER:
        print(f"Too high!\nTry again!")
        PLAYER_HEARTS-=1
    elif guess < RANDOM_NUMBER:
        print(f"Too low!\nTry again!")
        PLAYER_HEARTS-=1
    else:
        print("Must be a number")