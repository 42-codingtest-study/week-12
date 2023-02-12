# <정수론 심화>
# 16400
# 소수 화폐
# https://www.acmicpc.net/problem/16400

# dp 문제 유형
# python3로 제출하면 시간초과 - pypy3로 제출함

import sys
input = sys.stdin.readline

n = int(input())

# 에라토스테네스의 체를 이용한 소수 판별
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:  # 나누어 떨어지면 소수 x
            return False
    return True

prime_num = []

for i in range(2, n + 1):
    if is_prime(i):
        prime_num.append(i)

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for p in prime_num:
    for i in range(p, n + 1):
        dp[i] = (dp[i] + dp[i - p]) % 123456789

print(dp[n])