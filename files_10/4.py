# https://projecteuler.net/problem=4

def palindrome(num):
    return str(num) == str(num)[::-1]

N = 3
res = None

for i in range(10**(N-1), 10**N):
    for j in range(10**(N-1), 10**N):
        if palindrome(i*j):
            if res is None or res < i*j:
                res = i * j
                
print(res)