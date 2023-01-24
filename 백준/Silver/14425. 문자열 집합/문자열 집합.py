import sys

input = sys.stdin.readline

N, M = map(int, input().split())

test_a = []

for _ in range(N):
    test_a.append(input().strip())

cnt = 0

for _ in range(M):
    test_b = str(input().strip())

    if test_b in test_a:
        cnt += 1

print(cnt)
