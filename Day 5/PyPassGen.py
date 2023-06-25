import random

letters = ["a","b","c","d","e","f","g","h","j","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"
           "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
nums = ["1","2","3","4","5","6","7","8","9","0"]
syms = ["`","!","@","#","$","&","*","(",")","_","-","?"]




password = []
try:
    nr_lets = int(input("Number of letters? "))
    nr_syms = int(input("Number of Symbols? "))
    nr_nums = int(input("How many nums? "))
except ValueError:
    print("Must be num.")
    
for i in range(1,nr_lets+1):
    random_let= random.choice(letters)
    password.insert(random.randint(0,len(letters)),random_let)
for x in range(1,nr_nums+1):
    random_num = random.choice(nums)
    password.insert(random.randint(0,len(nums)),random_num)
for y in range(1,nr_syms+1):
    random_syms = random.choice(syms)
    password.insert(random.randint(0,len(syms)),random_syms)

random.shuffle(password)

newPass=""

for h in password:
    newPass+=h

print(f" Your super hard password is {newPass}")

