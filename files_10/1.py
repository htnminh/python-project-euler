# https://projecteuler.net/problem=1

N = 1000
res = 0

for i in range(1, N):
    if i % 3 == 0 or i % 5 == 0:
        res += i
print(res)