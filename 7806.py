# GCD!
# https://www.acmicpc.net/problem/7806

def fn(a) :
    num = a
    count = 0
    while num <= n:
        count += n // num
        num *= a
    return count

while True :
    try :
        N = input()
        if N == "" :
            break
    except :
        break
    n, k = map(int, N.split())
    if n == 0 :
        n = 1
    arr = []
    x = k
    for i in range(2, k + 1) :
        if i * i > k :
            break
        while x % i == 0 :
            arr.append(i)
            x //= i
    if x != 1 :
        arr.append(x)
    temp = set(arr)
    result = 1
    for i in temp :
        if fn(i) != 0 :
            num = min(fn(i), arr.count(i))
            result *= (i ** num)
    print(result)