import string
import random

if __name__ == "__main__":
    while True:
        S1 = string.ascii_lowercase
        S2 = string.ascii_uppercase
        S3 = string.digits
        S4 = string.hexdigits
        S5 = string.punctuation
        Passlen = int(input("enter your password length\n"))
        s = []
        s.extend(list(S1))
        s.extend(list(S2))
        s.extend(list(S3))
        s.extend(list(S4))
        # s.extend(list(S5))
        s.extend(list(S5))
        random.shuffle(s)
        print("your password is:")
        print("".join(s[0:Passlen]))
       