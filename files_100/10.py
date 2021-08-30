# https://projecteuler.net/problem=10

N = int(2E6)  # 2,000,000

res = 0
prime_list = [False, False]
prime_list += [True for i in range(N - 2)]

for i in range(2, N):
    if prime_list[i]:
        res += i
        for j in range(i*2, N, i):
            prime_list[j] = False
print(res)