# 소수 쌍
# https://www.acmicpc.net/problem/1017

# 시간초과가 너무난다 ...
# from itertools import combinations, permutations

# prime = [True] * 2001
# prime[0] = prime[1] = False
# for i in range(2, int(2000 ** 0.5) + 1) :
#     if prime[i] :
#         for j in range(2 * i, 2001, i) :
#             prime[j] = False
# N = int(input())
# lst = list(map(int, input().split()))
# first = lst[0]
# odd = first % 2
# answer = set()
# for comb in combinations(lst, len(lst) // 2) :
#     if (comb[0] != first) :
#         break
#     if sum([1 for i in comb if i % 2 == odd]) != len(comb) :
#         continue
#     # print(comb)
#     tmp = [i for i in lst if i not in comb]
#     for perm in permutations(tmp, len(tmp)) :
#         cnt = 0
#         # print(comb, perm)
#         if prime[comb[0] + perm[0]] == False :
#             continue
#         if perm[0] in answer :
#             continue
#         for i in range(len(perm)) :
#             if (prime[comb[i] + perm[i]]) :
#                 cnt += 1
#             else :
#                 break
#                 # print(comb[i], perm[i])
#         if cnt == len(tmp) :
#             answer.add(perm[0])
#             # print("here")
# if len(answer) == 0 :
#     print(-1)
# else :
#     print(*sorted(answer))

# 다시 풀어보기 (이분 매칭)
def dfs(x):
    global Y
    global matched
    global visited
    if visited[Y.index(x)] :
        return False
    visited[Y.index(x)] = True
    for y in Y :
        if x + y in primes:
            if y not in matched or dfs(matched[y]) :
                matched[y] = x
                return True
    return False

N = int(input())
lst = list(map(int, input().split()))
# 소수 목록을 미리 준비
prime = [True] * 2001
prime[0] = prime[1] = False
for i in range(2, int(2000 ** 0.5) + 1) :
    if prime[i] :
        for j in range(2 * i, 2001, i) :
            prime[j] = False
primes = [i for i in range(2001) if prime[i]]
answers = []
for i in lst :
    matched = {}
    if i == lst[0] :
        continue
    if lst[0] + i in primes :
        if N == 2 :
            answers.append(i)
            break
        Y = [j for j in lst]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y :
            visited = [False for _ in range(len(Y))]
            dfs(y)
    if N != 2 and len(matched) == N - 2 :
        answers.append(i)
if not answers :
    answers.append(-1)
answers.sort()
print(' '.join(list(map(str, answers))))
