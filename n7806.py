# <정수론 심화>
# 7806
# GCD!
# https://www.acmicpc.net/problem/7806

# 팩토리얼 사용하면 시간초과
# 시간초과

import sys
input = sys.stdin.readline

while 1:
    try:
        n, k = map(int, input().split())

    except:
        exit()

    n_nums = []
    n_dic = {}
    k_nums = []
    k_dic = {}

    # 소인수분해
    def factorization(x):
        d = 2
        number = []

        while x >= d:
            if x % d == 0:
                number.append(d)
                x /= d
            else:
                d += 1
        return number

    for i in range(2, n + 1):
        n_nums.extend(factorization(i))     # n! 소인수분해
    k_nums = factorization(k)   # k 소인수분해

    # 공통 인수 저장한 리스트
    a = [i for i in n_nums if i in k_nums]
    inter = list(set(a))  # set을 이용한 중복 제거

    # 인수 개수 파악을 위해 딕셔너리에 저장
    for i in n_nums:
        n_dic[i] = n_dic.get(i, 0) + 1

    for i in k_nums:
        k_dic[i] = k_dic.get(i, 0) + 1

    gcd = 1

    for i in inter:
        if n_dic[i] > k_dic[i]:
            gcd *= i ** k_dic[i]
        else:
            gcd *= i ** n_dic[i]

    print(gcd)