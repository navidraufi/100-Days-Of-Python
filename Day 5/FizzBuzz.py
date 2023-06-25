fizz = "Fizz"
buzz = "Buzz"

try:
    num = int(input("Type the num: "))
    divByThree = (num%3 == 0)
    divByFive = (num%5 == 0)
    if divByFive and divByThree:
        print(fizz+buzz)
    elif divByFive:
        print(buzz)
    elif divByThree:
        print(fizz)
    else:
        print(num)
except ValueError:
    print("Must be a num.")
