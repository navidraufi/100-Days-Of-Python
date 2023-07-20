def calculate_score(score, total_score):
    percent = round(((score * 100) / total_score),2)
    if percent > 90:
        print(f"You got {percent}% out of {100}%.\nWhich is an (A) score.")
    elif percent > 80:
        print(f"You got {percent}% out of {100}%.\nWhich is a (B) score.")
    elif percent > 70:
        print(f"You got {percent}% out of {100}%.\nWhich is a (C) score.")
    elif percent > 60:
        print(f"You got {percent}% out of {100}%.\nWhich is a (D) score.")
    else:
        print(f"You got {percent}% out of {100}%.\nAnd unfortunately you failed.")

