
def converter(number):
    result = []
    final_result = ""
    if number > 0:
        
        while number != 0:
            mode = int(number % 2)
            result.insert(len(result),mode)
            number = int(number / 2)
    elif number<0:
        result.append(1)
        while number!= 0:
            mode = int(number % 2)
            result.insert(len(result),mode)
            number = int(number / 2)
    result.reverse()
    for i in result:
        final_result+=(str(i)+" ")
    print(f"The decimal number {number} is equal to {final_result}.")
    
    
    
