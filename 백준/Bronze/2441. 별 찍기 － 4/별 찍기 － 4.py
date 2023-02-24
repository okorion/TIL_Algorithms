import sys
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    print((_) * " " + (N - _) * "*")
