# https://projecteuler.net/problem=5

'''
1  = 1
2  = 2
3  = 3
4  = 2**2
5  = 5
6  = 2 * 3
7  = 7
8  = 2**3
9  = 3**2
10 = 2 * 5

2**3 * 3**2 * 5 * 7 = 2520

2**log2(10) = 10
2**int(log2(10)) = 2**3 = 8
        ...
'''

from math import log

N = 20
prime_dict = dict()
res = 1

for i in range(2, N+1):
    if i not in prime_dict:
        prime_dict[i] = True
        for j in range(i*2, N+1, i):
            prime_dict[j] = False
    
    if prime_dict[i]:
        res *= i ** int(log(N, i))

print(res)