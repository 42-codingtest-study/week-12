# 소수 부분 문자열
# https://www.acmicpc.net/problem/5636

import sys
input = sys.stdin.readline
prime = [True] * (100001)
prime[0] = prime[1] = False
for i in range(2, int(100000 ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, 100001, i) :
            prime[j] = False
# prime_lst = [i for i in range(100001) if prime[i]]
while (1) :
    n = input()
    nlen = len(n)
    if int(n) == 0 :
        break
    if nlen > 5 :
        nlen = 5
    while nlen > 0 :
        tmp_lst = []
        for i in range(len(n) - nlen) :
            tmp = n[i : i + nlen]
            if prime[int(tmp)] and int(tmp) > 10 ** (nlen - 1) :
                tmp_lst.append(tmp)
        if len(tmp_lst) != 0 :
            print(max(tmp_lst))
            break
        nlen -= 1