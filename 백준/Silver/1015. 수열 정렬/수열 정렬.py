import sys

input = sys.stdin.readline

N = int(input())

res = list(map(int, input().split()))
visited = [0] * N

new_res = sorted(res)   # 1 1 2 3

for idx, val in enumerate(new_res):   # 1 1 2 3
    visited[res.index(val)] = idx
    res[res.index(val)] = 0   # 2 1 3 1

print(*visited)
