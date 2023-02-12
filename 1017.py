#소수 쌍

import sys
import math
 
def dfs(x):
    global b
    global matched
    global visited
    if visited[b.index(x)]: return False
    visited[b.index(x)] = True
    for y in b:
        if x + y in primes:
            if y not in matched or dfs(matched[y]):
                matched[y] = x
                return True
    return False
 
N = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))

primes = []
for i in range(2, 2000):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime: primes.append(i)
    else: continue
 
answers = []
for i in a:
    matched = {}
    if i == a[0]: continue
    if a[0] + i in primes:
        if N == 2:
            answers.append(i)
            break
        
        b = [x for x in a]
        del b[0]
        del b[b.index(i)]
        matched = {}
        for y in b:
            visited = [False for _ in range(len(b))]
            dfs(y)
    
    if N != 2 and len(matched) == N - 2: answers.append(i)
 
if not answers:
    answers.append(-1)
 
answers.sort()
 
print(' '.join(list(map(str, answers))))