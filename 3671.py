# 산업 스파이의 편지
# https://www.acmicpc.net/problem/3671

from itertools import combinations, permutations

import sys
input = sys.stdin.readline
prime = [True] * 10000001
prime[0] = prime[1] = False
for i in range(int(10000000 ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, 10000001, i) :
            prime[j] = False

for _ in range(int(input())) :
    n = list(input().replace("\n", ""))
    answer = set()
    for i in range(1, len(n) + 1) : # 몇개의 숫자를 사용할지 결정
        for comb in combinations(n, i) :    # 숫자 조합 생성
            for perm in permutations(comb, i) : # 조합을 토대로 순열 생성
                if prime[int(''.join(perm))] :  # 그 순열이 소수라면
                    answer.add(int(''.join(perm)))  # 정답에 추가
    print(len(answer))
