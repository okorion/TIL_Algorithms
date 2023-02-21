import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
parents = list(range(N+1))


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a > b:
        parents[a] = b

    else:
        parents[b] = a


for i in range(1, N + 1):
    maps = list(map(int, input().split()))

    for j in range(1, len(maps) + 1):
        if maps[j - 1] == 1:
            union(i, j)

tour = list(map(int, input().split()))
result = set([find(i) for i in tour])

if len(result) >= 2:
    print("NO")
else:
    print("YES")

