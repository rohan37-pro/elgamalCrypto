import string

cipher = list(eval(input("Enter Cipher : ")))

message = []

beta = None
while len(message)<len(cipher):
    
    for c in cipher:
        for m in string.printable:
            if beta == None:
                beta 