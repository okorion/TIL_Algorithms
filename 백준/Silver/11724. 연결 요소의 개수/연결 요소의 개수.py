import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(start, depth):
    visited[start] = True

    for _ in graph[start]:
        if not visited[_]:
            dfs(_, depth+1)


N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
cnt = 0

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for _ in range(1, N+1):
    if not visited[_]:
        if not graph[_]:
            cnt += 1
            visited[_] = True
        else:
            dfs(_, 0)
            cnt += 1

print(cnt)
