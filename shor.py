import math

def find_factors(n):
    a = math.ceil(math.sqrt(n))
    b2 = a * a - n
    while not math.sqrt(b2).is_integer():
        a += 1
        b2 = a * a - n
    return (a - math.sqrt(b2), a + math.sqrt(b2))

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

n = 961752149
factors = find_factors(n)

if is_prime(n):
    print("The number is prime")
else:
    print(factors)
    res = factors[0] * factors[1] == n
    if res:
        print("The factors are correct")
    else:
        print("The factors are wrong")
