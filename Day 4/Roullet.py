import random

names = input("Give me everybody`s names, separated by a comma (,): ")

guys = names.split(", ")

total_guys = len(guys) - 1
random_num = random.randint(0,total_guys)
result = guys[random_num]

print(f"Today, {result} is going to pay the bill.")