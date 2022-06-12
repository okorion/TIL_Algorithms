import sys

M, N = list(map(int, sys.stdin.readline().split()))

ref_table = [0] * 2 + [1] * 1000001


for i in range(2, 500001):
    for _ in range(2*i, len(ref_table), i):
        ref_table[_] = 0

for j in range(M, N+1):
    if ref_table[j] == 1:
        print(j)