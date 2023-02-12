# <정수론 심화>
# 23048
# 자연수 색칠하기
# https://www.acmicpc.net/problem/23048

# 시간초과

import sys
input = sys.stdin.readline

n = int(input())
num = []

for i in range(1, n + 1):
    num.append(i)   # 자연수 리스트

color = 0
number = [0] * n

for i in num:
    if i == 1:
        color += 1
        number[i - 1] = color

    else:
        color += 1
        for j in num:
            if j % i == 0:
                if number[j - 1] == 0:
                    number[j - 1] = color
'''
    else:
        color += 1
        for j in num[i - 1 : ]:
            if j % i == 0:
                if number[j - 1] == 0:
                    number[j - 1] = color
'''

result = list(set(number))  # set을 이용한 중복 제거

print(len(result))