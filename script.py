import random


DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']

UPCAST_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']

SYMBOLS = ['@', '#', '$',  ':', '.', '~', '*', '&']

while True:
    password_length = int(input("enter your password length:"))
    password_count = int(input("number of password do you need:"))
    if password_count ==999:
        break 
    random.shuffle(DIGITS)
    random.shuffle(LOCASE_CHARACTERS)
    random.shuffle(UPCAST_CHARACTERS)
    random.shuffle(SYMBOLS)
    s = []
    s.extend(list(DIGITS))
    s.extend(list(LOCASE_CHARACTERS))
    s.extend(list(UPCAST_CHARACTERS))
    s.extend(list(SYMBOLS))
    for x in range(password_count):
        print("your password is:", end="_") 
        print("".join(random.sample(s, password_length)))
