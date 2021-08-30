# https://projecteuler.net/problem=6

N = 100
sum_squares = 0

for i in range(1, N+1):
    sum_squares += i ** 2

square_sum = (N * (N+1) / 2)**2

print(int(abs(sum_squares - square_sum)))