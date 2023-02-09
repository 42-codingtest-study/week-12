# 소수 화폐
# https://www.acmicpc.net/problem/16400

N = int(input())
prime = [True] * (N + 1)
prime[0] = prime[1] = False
for i in range(2, int(N ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, N + 1, i) :
            prime[j] = False
prime_lst = [i for i in range(N + 1) if prime[i]]
dp = [0] * (N + 1)
dp[0] = 1
for i in prime_lst :
    for j in range(i, N + 1) :
            dp[j] += dp[j - i] % 123456789
print(dp[-1] % 123456789)
