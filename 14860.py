# GCD 곱
# https://www.acmicpc.net/problem/14860

from math import gcd
N, M = map(int, input().split())
answer = 1
for i in range(1, N + 1) :
    for j in range(1, M + 1) :
        answer *= (gcd(i, j) % (10 ** 9 + 7))
print(answer)
