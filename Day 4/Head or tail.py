import random
import time

player_1 = input("Type player one`s name: ")
player_1_side = input("Which side do you choose? ").lower
player_2 = input("Type player two`s name: ")
player_2_side = input("Which side do you choose? ").lower

time.sleep(1)
print("3s")
time.sleep(1)
print("2s")
time.sleep(1)
print("1s")
time.sleep(1)

head_And_tail = ["Head","Tail"]
ran_num = random.randint(0,1)

result= head_And_tail[ran_num]
low_res = head_And_tail[ran_num].lower

if player_1_side == low_res:
    print(f"The result is {result}.\nAnd {player_1} wins.")
else:
    print(f"The result is {result}.\nAnd {player_2} wins.")


