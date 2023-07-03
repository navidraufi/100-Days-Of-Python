

def encrypt():
    text = input("Type the message you wanna encrypt bellow: \n")
    shift = int(input("What is the secret? "))
    encryptedMessage = ""
    for letter in text:
        encrypted = ord(letter)
        encrypted-=shift
        newMessage = chr(encrypted)
        encryptedMessage+=newMessage
    print(encryptedMessage)


def decrypt():
    text = input("Type the message you wanna decrypt bellow: \n")
    shift = int(input("What is the secret? "))
    decryptedMessage = ""
    for letter in text:
        encrypted = ord(letter)
        encrypted+=shift
        newMessage = chr(encrypted)
        decryptedMessage+=newMessage
    print(decryptedMessage)

choice = input("Do you want to encrypt or decrypt? ").lower()

if choice == "encrypt":
    encrypt()
elif choice == "decrypt":
    decrypt()
else:
    print("I do not understand.")
