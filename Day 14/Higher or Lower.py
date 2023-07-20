import random

accounts = [{
    "name": "Instagram",
    "follower_count": 346,
    "description": "Social media platform",
    "country": "United States"
}, {
    "name": "C. Ronaldo",
    "follower_count": 244,
    "description": "Football Player",
    "country": "Portugal"
}, {
    "name": "Mia Khalifa",
    "follower_count": 1000,
    "description": "Pornstar",
    "country": "United States"
}, {
    "name": "Sha Rukh Khan",
    "follower_count": 255,
    "description": "Actor",
    "country": "India"
}, {
    "name": "Johnny Sins",
    "follower_count": 366,
    "description": "Pornstar",
    "country": "United States"
}, {
    "name": "Weeknd",
    "follower_count": 599,
    "description": "Singer",
    "country": "United States"
}]


def rand_account(list_of_account):
    random_account = random.choice(accounts)
    accounts.pop(accounts.index(random_account))
    return random_account


def compare(first, second):
    if first["follower_count"] > second["follower_count"]:
        return True
    else:
        return False


total_score = 0


first_account = rand_account(accounts)

while True:
    if len(accounts) == 0:
        print(f"You win!\nBecause there is nothing left.\nYour score is {total_score}.")
        break
    
    
    second_account = rand_account(accounts)

    print(f"{first_account['name']}, a {first_account['description']} from {first_account['country']}.")
    print("VS.")
    print(f"{second_account['name']}, a {second_account['description']} from {second_account['country']}.")

    answer = input("Which one has more followers? 'a' or 'b' \n").lower()

    if answer == "a":
        if compare(first_account, second_account):
            total_score += 1
            first_account = first_account
        else:
            print("You lose!")
            print(f"Your score is {total_score}")
            total_score = 0
            break
    else:
        if compare(second_account, first_account):
            total_score += 1
            first_account = second_account
        else:
            print("You lose!")
            print(f"Your score is {total_score}")
            total_score = 0
            break
