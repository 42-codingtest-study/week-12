#소수 부분 문자열(에라토스테네스의 체)

def input(n):
    li = [1] * (n + 1)
    for i in range(2, int(n ** 0.5) + 1):
        if li[i]:
            for j in range(i + i, n + 1, i):
                li[j] = 0
    p = [i for i in range(2, n + 1) if li[i]]
    return p

while 1:
    s = input()
    if s == '0':
        break
    p = input(100000)
    res = 2
    for n in p:
        if str(n) in s:
            res = n
    print(res)