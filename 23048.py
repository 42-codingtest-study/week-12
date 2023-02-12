n = int(input())

result = 0
prime_list = []
for i in range(n + 1):
    prime_list.append(i)
prime = [True] * (n + 1)

change = 2
for i in range(2, n + 1):
    if prime[i] == True:
        prime_list[i] = change
        for j in range(2 * i, n + 1, i):
            prime[j] = False
            if prime_list[j] == j:
                prime_list[j] = j
        change += 1


for i in range(1, n + 1) :
    if prime[i] :
        result += 1
print(result)
for i in range(1, n + 1):
    print(prime_list[i], end=' ')


