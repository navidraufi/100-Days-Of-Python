from math import ceil

def amountOfCans(height,width):
    area = height*width
    cans = int(ceil((area/5)))
    print(f"The amount of cans required to paint your wall is {cans}.")
    
    
amountOfCans(3,9)