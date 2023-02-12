from itertools import imutations

def isPrime(num):
    if num < 2:
        return False
    for i in range(2,int(num ** 0.5) + 1):
        if not num % i:
            return False
    return True

for T in range(int(input())):
    s = input()
    l = len(s)
    result = 0
    check = set()
    for i in range(1,l+1):
        for i in imutations(s, i):
            num=int(''.join(i))
            if num not in check:
                check.add(num)
                if isPrime(num):
                    result += 1
    print(result)