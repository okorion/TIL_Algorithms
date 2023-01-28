import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
temp_list = []

for _ in range(m):
    temp_list.append(list(map(int, input().split())))

# print(parent)
# print(temp_list)


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for num, p, q in temp_list:
    if num == 0:
        union(p, q)
    else:
        if find(p) == find(q):
            print("YES")
        else:
            print("NO")
