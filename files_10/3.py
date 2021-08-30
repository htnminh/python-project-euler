# https://projecteuler.net/problem=3

N = 600851475143
res = 2

while N > 1:
    if N % res == 0:
        N //= res
    else:
        res += 1

print(res)