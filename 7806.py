
from collections import Counter

def res_prime(n):
    arr = []
    n_copy = n
    for i in range(2, n + 1):
        if i * i > n:
            break
        while n_copy % i == 0:
            arr.append(i)
            n_copy //= i
    if n_copy != 1:
        arr.append(n_copy)
    return(Counter(arr).items())

def GCD(n, k):
    if n == 0:
        return 1
    
    else:
        factor = res_prime(k)
        res = 1
        for prime, count_number in factor:
            p = prime
            count = 0
            while p <= n:
                count += n//p
                p *= prime
            res *= pow(prime, min(count_number, count))
        return res

try:
    while 1:
        n, k = map(int, input().split())
        print(GCD(n,k))
    
    # print(math.gcd(n_list, k_list))
        
except EOFError:
    exit()