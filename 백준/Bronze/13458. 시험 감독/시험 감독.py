import sys
import math

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
cnt = 0

for a in A:
    if a - B > 0:
        cnt += math.ceil((a-B)/C)

result = N + cnt

print(result)
