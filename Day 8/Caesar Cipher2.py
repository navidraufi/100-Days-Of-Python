alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'," ",".",
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~'," ","."
            ]

def encrypt():
    text = input("Type your message: ")
    shift = int(input("Enter the secret code: "))
    message = ""

    for letter in text:
        letterPosition = alphabet.index(letter)
        new_position = letterPosition+shift
        message+= alphabet[new_position]
    print(f"The encrypted message is \n'{message}' and the secret code is {shift}.")


def decrypt():
    text = input("Type your encrypted message: ")
    shift = int(input("Enter the secret code: "))
    demessage = ""

    for letter in text:
        letterPosition = alphabet.index(letter)
        new_position = letterPosition-shift
        demessage+= alphabet[new_position]
    print(f"The secret message is \n'{demessage}'")


def begin():
    isStopped = False
    while not isStopped:
        direction = input("Type encode to encrypt and decode to decrypt or stop to quit: \n").lower()
        if direction == "encode":
            encrypt()
        elif direction == "decode":
            decrypt()
        elif direction == "stop":
            break
        else:
            print("I do not understand.")
            begin
begin()