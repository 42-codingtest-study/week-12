
def prime(n) :
    arr = [True] * (n)
    for i in range(2, int(n ** 0.5) + 1) :
        if(arr[i] == True) :
            for j in range(i + i, n, i) :
                arr[j] = False
    return [i for i in range(2, n) if arr[i] == True]

while(True) :
    n = int(input())
    res = 2
    if n == 0 :
        break
    sum = prime(100000)
    for i in sum :
        if(str(i) in str(n)) :
            res = i
    print(res)
        
