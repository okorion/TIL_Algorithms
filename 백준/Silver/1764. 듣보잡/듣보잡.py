import sys

input = sys.stdin.readline

N, M = map(int, input().split())
a = []
b = []

for num in range(N):
    a.append(input().strip())
for num in range(M):
    b.append(input().strip())

a = set(a)
b = set(b)
c = []

result = sorted(list(a & b))

print(len(result))
for tc in sorted(result):
    print(tc)
