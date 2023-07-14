from os import system
import random
import time


def main():    


    cards_available = [11,2,3,4,5,6,7,8,9,10,10,10,10]


    def replace(list_,item,withWhat):
        index = list_.index(item)
        list_.pop(index)
        list_.insert(index,withWhat)

    
    # def random_card(x):
    #     return random.choice(x)
    def random_card(x):
        random_number = random.choice(x)
        random_number_index = x.index(random_number)
        x.pop(random_number_index)
        
        return random_number
    
    def calculate_cards(cards_deck):
    
        if sum(cards_deck) > 21 and 11 in cards_deck:
            replace(cards_deck,11,1)
    
        return sum(cards_deck)

    game_stop = True

    player_cards = [random_card(cards_available),random_card(cards_available)]
    computer_cards = [random_card(cards_available),random_card(cards_available)]


    def game_over():

        game_stop = False    
        player_total = calculate_cards(player_cards)
        computer_total = calculate_cards(computer_cards)
        if player_total > computer_total:
            print("Player wins!")
            print(f"Your cards are {player_cards}.")
            print(f"Computer cards are {computer_cards}.")
        elif player_total == computer_total:
            print("Draw!")    
            print(f"Your cards are {player_cards}.")
            print(f"Computer cards are {computer_cards}.")

        else:
            print("Computer wins!")
            print(f"Your cards are {player_cards}.")
            print(f"Computer cards are {computer_cards}.")



    
    while game_stop:
        if sum(player_cards) == 21 and len(player_cards) == 2:
            print("Player has Black Jack!")
            print(f"Your cards are {player_cards}.")
            print(f"Computer cards are {computer_cards}.")
            break
        if sum(computer_cards) == 21 and len(computer_cards) == 2:
            print("Computer has Black Jack!")
            print(f"Your cards are {player_cards}.")
            print(f"Computer cards are {computer_cards}.")
            break
            
        another =input(f"Your cards are {player_cards} and the computers first hand is {computer_cards[0]}.\nDo you wanna take another card?  'Y' or 'N' \n")
        player_total = calculate_cards(player_cards)
        computer_total = calculate_cards(computer_cards)

        if another == "y":
            player_cards.append(random_card(cards_available))
            player_total = calculate_cards(player_cards)
            if player_total > 21:
                print("Player Lose!")
                print(f"Your cards are {player_cards}.")
                print(f"Computer cards are {computer_cards}.")
                game_stop = False
                break
            
            
            if sum(computer_cards) <17 :
                computer_cards.append(random_card(cards_available))
                computer_total = calculate_cards(computer_cards)
                if computer_total > 21:
                    print("Computer lose!")
                    print(f"Your cards are {player_cards}.")
                    print(f"Computer cards are {computer_cards}.")
                    game_stop = False
                    break
                
        else:
            if sum(computer_cards) <17 :
                computer_cards.append(random_card(cards_available))
                computer_total = calculate_cards(computer_cards)
                if computer_total > 21:
                    print("Computer lose!")
                    print(f"Your cards are {player_cards}.")
                    print(f"Computer cards are {computer_cards}.")
                    game_stop = False
                    break
                
            game_stop = False
            game_over()

is_playing = True

def dividing(time_count):
    hi = 1
    while time_count > 0:
        time.sleep(0.2)
        print("%-10s" % "." * hi )
        time_count -=1
        hi+=1
         

while is_playing:
    game_start = input("\n\nDo you want to play the game of Black Jack? 'Y' or 'N' \n").lower()
    if game_start == "y":
        system("cls")
        dividing(6)
        main()
    elif game_start == "n":
        print("OK\nWhy so serious?")
        is_playing = False
    else:
        print("Yo no comprendo amigo!")