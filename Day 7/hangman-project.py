import random

words_list = ["dog","cat","evil","scorpion"]
length = len(words_list)

chosen_word = words_list[random.randint(0,length-1)]

game_is_won = False
length_of_cho = len(chosen_word)

answer = []
display = []
lives = 6

for i in range(length_of_cho):
    letter = chosen_word[i]
    answer.append(letter)

for _ in range(length_of_cho):
    display.append("_")

print(display)
while not game_is_won:
    
    if lives == 0:
        print("You lose!")
        game_is_won =True
        break
    guess = input("Guess a letter? ")

    for position in range(length_of_cho):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess
    if guess not in chosen_word:
        lives-=1
        print(f"You have {lives} left.")
        
    
    print(display)
        
    if "_" not in display:
        print("You have won!")
        game_is_won = True