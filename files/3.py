# https://projecteuler.net/problem=3

N = 600851475143
res = None
prime = dict()

for i in range(2, N):
    if i not in prime:
        prime[i] = True
        if res is None or res < i:
            res = i
        for j in range(2*i, N+1, i):
            prime[j] = False

print(res)