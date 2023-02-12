# <정수론 심화>
# 5636
# 소수 부분 문자열
# https://www.acmicpc.net/problem/5636

#import sys
#input = sys.stdin.readline

# 에라토스테네스의 체를 이용한 소수 판별
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:  # 나누어 떨어지면 소수 x
            return False
    return True

while 1:
    s = input()
    prime_list = []

    if s == '0':    # 종료
        exit()

    max = 5    # 100000보다 작거나 같은 소수이므로 최대 자리수 5

    for i in range(0, len(s) - 1 - max):
        check = s[i : i + max - 1]

        if is_prime(check):
            prime_list.append(check)

    if len(prime_list) == 0:
        max -= 0

        for i in range(0, len(s) - 1 - max):
            check = s[i: i + max - 1]

            if is_prime(check):
                prime_list.append(check)