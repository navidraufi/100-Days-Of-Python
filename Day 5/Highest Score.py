score  =  input("Enter the scores of the students.\n").split(" " or "," or ", ")
highest_score = 0
for i in score:
    new = int(i)
    if new > highest_score:
        highest_score = new
print(f"The highest score in the class is {highest_score}.")

