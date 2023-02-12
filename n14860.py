# <정수론 심화>
# 14860
# GCD 곱
# https://www.acmicpc.net/problem/14860

# 시간초과

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def gcd(x, y):
    x, y = (x, y) if x > y else (y, x)

    while y:
        x, y = y, x % y

    return x

result = 1
for i in range(1, n + 1):
    for j in range(1, m + 1):
        result *= gcd(i, j)

print(result % (10 ** 9 + 7))