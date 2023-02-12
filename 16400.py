#소수 화폐, DP
#시간 초과 > pypy3 제출

import math

def is_input(number):
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

n = int(input())
input = []

for i in range(2, n + 1):
    if is_input(i):
        input.append(i)

dp = [0 for _ in range(n + 1)]
dp[0] = 1

for p in input:
    for i in range(p, n + 1):
        dp[i] = (dp[i] + dp[i - p]) % 123456789
            
print(dp[n])