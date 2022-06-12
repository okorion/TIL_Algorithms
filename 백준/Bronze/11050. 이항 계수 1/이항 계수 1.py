import sys

N, K = list(map(int, sys.stdin.readline().split()))

temp_num = 1

for a in range(N, N-K, -1):
    temp_num *= a

for b in range(1, K+1):
    temp_num /= b

print(int(temp_num))
