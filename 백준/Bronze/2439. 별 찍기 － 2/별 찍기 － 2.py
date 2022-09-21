import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print(" " * (N-1-_) + "*" * (_+1))
