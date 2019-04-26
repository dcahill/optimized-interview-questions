# definitely not the fastest as it's 2 to n - 1
# including 2 to n2 (squared)

def list_primes(n):
    for num in range(2, n):
        is_prime = True
        for i in range(2, num):
            if num % i == 0: is_prime = False
        if is_prime: print(num)

#not working yet and I'm exhausted
def list_primes_v2(n):
    for i in range(2, n):
        is_prime = True if (n % i != 0 for i in range(2, int(n ** 0.5) + 1)) else False
    if is_prime: print(i)


list_primes(10)
#list_primes_v2(101)
