# https://projecteuler.net/problem=7

N = 10001
MAX_SIZE = int(1E7)

count = 0
prime_list = [False, False]
prime_list += [True for i in range(MAX_SIZE - 2)]

for i in range(2, MAX_SIZE):
    if prime_list[i]:
        count += 1
        if count == N:
            print(i)
            break
        for j in range(i*2, MAX_SIZE, i):
            prime_list[j] = False