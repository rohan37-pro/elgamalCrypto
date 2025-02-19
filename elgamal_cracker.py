import string
import time

slow = 0.05

cipher = list(eval(input("Enter Cipher : ")))
print()

message = []

beta = None
start = 0
start_again = True
while start<len(string.printable) :
    if start_again:
        beta = int(cipher[0] / ord(string.printable[start]))
        start_again = False
        message.append(string.printable[start])
        print("".join(message), end='\r')
        time.sleep(slow)
    for  c in cipher[1:]:
        for m in string.printable:
            if int(c/ord(m)) == beta:
                time.sleep(slow)
                message.append(m)
                print("".join(message), end='\r')
                found = True
                break
        else:
            start+=1
            start_again = True
            message = []
            break
    if len(message)==len(cipher):
        print(f"\"{''.join(message)}\"")
        start+=1
        start_again = True
        message = []