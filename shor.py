import math

def shore(n):
    a = math.ceil(math.sqrt(n))
    print(a)
    b2 = a*a - n
    print(b2)
    while not math.sqrt(b2).is_integer():
        a += 1
        print(a)
        b2 = a*a - n
        print(b2)
    return (a - math.sqrt(b2), a + math.sqrt(b2))

n = 15
factors = shore(n)
print(factors)
