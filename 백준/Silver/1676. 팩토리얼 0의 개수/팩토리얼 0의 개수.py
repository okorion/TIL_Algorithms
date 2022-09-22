import sys

input = sys.stdin.readline

N = int(input())
cnt = 0

for _ in range(1, N+1):
    if _ % 125 == 0:
        cnt += 3
    elif _ % 25 == 0:
        cnt += 2
    elif _ % 5 == 0:
        cnt += 1

print(cnt)
