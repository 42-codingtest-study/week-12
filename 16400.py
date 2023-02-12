n = int(input())

prime = [2]

for i in range(3, n + 1):
    for p in prime:
        if i % p == 0:
            break
    else:
        prime.append(i)
# print(prime)
res = []        
for _ in range(n + 1):
    res.append(0)
res[0] = 1

# print(res)
for p in prime:
    # print ('P:', p)
    for i in range(p, n + 1):
        # print(res)
        res[i] = (res[i] + res[i-p]) % 123456789
# print(res)
print(res[-1])