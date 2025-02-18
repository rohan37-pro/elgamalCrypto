import random


ALPHA = None
BETA = None
CIPHER = []
k = None
a = None
PRIME = None


def generate_prime(bits):
    p = random.randint(2**bits, 2**(bits+1))
    while not is_prime(p):
        p = random.randint(2**bits, 2**(bits+1))
    return p



def is_prime(p):
    if p%2==0:
        return False
    for i in range(3, int(p**0.5)+1, 2):
        if p%i==0:
            return False
    else:
        return True
    

def encrypt(msg):
    pass

def decrypt():
    pass


if __name__ == "__main__":
    prime_bits = 2048
    PRIME = generate_prime(prime_bits)
    ALPHA = random.randint(1, PRIME - 1)
    a = random.randint(1, PRIME - 1)
    BETA = (ALPHA**a) % PRIME
    k = random.randint(1, PRIME -1 )
    y = (ALPHA**k) % PRIME
    