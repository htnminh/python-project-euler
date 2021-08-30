# https://projecteuler.net/problem=2

N = 4e6
res = 0
prev, curr = 1, 2

while curr <= N:
    if curr % 2 == 0:
        res += curr

    next = prev + curr
    prev = curr 
    curr = next

print(res)