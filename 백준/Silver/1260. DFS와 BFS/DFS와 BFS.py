import sys
from collections import deque

INF = int(1e9)

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[0] * (N+1) for _ in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)


def dfs(start):
    visited_dfs[start] = 1
    print(start, end=" ")

    for _ in range(1, N+1):
        if graph[start][_] == 1 and visited_dfs[_] == 0:
            dfs(_)


def bfs(start):
    queue = deque()
    queue.append(start)
    visited_bfs[start] = 1

    while queue:
        dx = queue.popleft()
        print(dx, end=" ")
        for _ in range(1, N+1):
            if visited_bfs[_] == 0 and graph[dx][_] == 1:
                queue.append(_)
                visited_bfs[_] = 1


for _ in range(M):
    a, b = map(int, input().split())

    graph[a][b] = 1
    graph[b][a] = 1

# print(graph)

dfs(V)
print()
bfs(V)
