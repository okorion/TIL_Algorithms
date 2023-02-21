import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parents = list(range(n+1))


def union(x, y):
    x = find(x)
    y = find(y)

    if x > y:
        parents[x] = y
    else:
        parents[y] = x


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])

    return parents[x]


for _ in range(m):
    a, b = map(int, input().split())

    if find(a) == find(b):
        print(_ + 1)
        exit(0)
        
    union(a, b)

else:
    print(0)
