from os import system
import random
import time


cards_available = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def thinking(timeTotalt):
    while timeTotalt > 0:
        time.sleep(1)
        print(f"Calculating! wait for {timeTotalt}.")
        timeTotalt-=1
print("Hello and welcome to BlackJack\\21")
is_player_playering = input("Do you wanna play the game of BlackJack? 'Y' 'N' \n").lower()





def choose_card(list):
    value = random.choice(list)
    return value

def calculate_value(first,second,third):
    return first+second+third

player_first = choose_card(cards_available)
player_second = choose_card(cards_available)
player_third = 0
player_overall = calculate_value(player_first,player_second,player_third)
player_list = [player_first,player_second]

computer_first = choose_card(cards_available)
computer_second = choose_card(cards_available)
computer_third = 0
computer_overall = computer_first+computer_second
other_computer_overall = computer_first+computer_second
computer_list_hidden = [computer_first,"???"]
computer_list_shown = [computer_first,computer_second]

def show_value():
    print(f"Player values are {player_list}")
    print(f"Computer values are {computer_list_shown}.")

def end_the_game():
    if player_overall > computer_overall:
        show_value()
        print("Player Wins!")
    else:
        show_value()
        print("Computer wins!")

print(player_overall)
print(computer_overall)

def computer_needs_more():
    if other_computer_overall < 17:
        computer_third = choose_card(cards_available)
        computer_list_shown.append(computer_third)
        computer_overall = calculate_value(computer_first,computer_second,computer_third)
        if computer_overall > 21:
            print("Computer loses!")
            print("PLayer wins!")
        else:
            end_the_game()


def player_wants_more():
    add_more = input("Do you wanna take another card? 'Y' 'N' \n").lower()
    if add_more == "y":
        player_third = choose_card(cards_available)
        player_overall = calculate_value(player_first,player_second,player_third)
        player_list.append(player_third)
        if player_overall > 21:
            show_value()
            print("Computer wins!")
            print("You lose!")
        else:
            computer_needs_more()
            end_the_game()
    else:
        computer_needs_more()
        end_the_game()    
        

def main():
    thinking(3)
    print(f"Player values are {player_list}")
    print(f"Computer values are {computer_list_hidden}.")
    player_wants_more()



main()
        
   
   
    

