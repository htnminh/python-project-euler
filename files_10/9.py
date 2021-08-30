# https://projecteuler.net/problem=9
'''
a < b < c < N

0 < a < N-2
a < b < N-1
b < c < N
'''
N = 1000

for a in range(1, N-2):
    for b in range(a+1, N-1):
        c = 1000 - (a+b)
        if int(a**2 + b**2) == int(c**2):
            print(a * b * c)
            break