# 자연수 색칠하기
# https://www.acmicpc.net/problem/23048

N = int(input())
thdlstn = [i for i in range(N + 1)]
prime = [True] * (N + 1)
prime[0] = prime[1] = False
for i in range(2, int(N ** 0.5) + 1):
    if prime[i]:
        for j in range(2 * i, N + 1, i) :
            prime[j] = False
            if thdlstn[j] == j :
                thdlstn[j] = i
prime_lst = [i for i in range(N + 1) if prime[i]]
for i in range(1, N + 1) :
    if prime[thdlstn[i]] :
        thdlstn[i] = prime_lst.index(thdlstn[i]) + 2
print(max(thdlstn[1 : ]))
print(*thdlstn[1 : ])
