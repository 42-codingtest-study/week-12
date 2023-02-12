# <정수론 심화>
# 3671
# 산업 스파이의 편지
# https://www.acmicpc.net/problem/3671

# 1276543 입력 시 1336이 아닌 7180이 나옴

import sys
input = sys.stdin.readline

import itertools

# 에라토스테네스의 체를 이용한 소수 판별
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:  # 나누어 떨어지면 소수 x
            return False
    return True

c = int(input())

for _ in range(c):
    n = input()
    number = list(n)

    # 하나의 문자로만 이루어져 있는 경우
    if n.count('1') == len(n) or n.count('2') == len(n) or n.count('3') == len(n) or n.count('4') == len(n) or n.count('5') == len(n) or n.count('6') == len(n) or n.count('7') == len(n) or n.count('8') == len(n) or n.count('9') == len(n):
        n = int(n[0:1])

        if is_prime(n):
            print(1)
        else:
            print(0)
    else:
        s_list = []     # 부분집합 넣을 리스트
        num_list = []   # 부분집합 정수 변환해서 넣을 리스트

        for i in range(1, len(number) + 1):
            tmp = itertools.permutations(number, i)
            s_list.extend(tmp)

        for i in s_list:
            s = ''
            for j in range(len(i)):
                s += i[j]

            if s.startswith('0'):    # 0으로 시작하는 경우 삭제
                s.lstrip('0')
            num_list.append(int(s))

        final_num_list = list(set(num_list))    # set을 사용해서 리스트 중복 제거

        for i in final_num_list:
            if i < 2:
                final_num_list.remove(i)

        for i in final_num_list:
            if is_prime(i):
                pass
            else:
                final_num_list.remove(i)

        print(len(final_num_list))