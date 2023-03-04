import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [[] for _ in range(N + 1)]


def dfs(i):
    for _ in graph[i]:
        if visited[_] == 0:
            visited[_] = i
            dfs(_)


visited = [0] * (N + 1)

for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


dfs(1)

for _ in range(2, N + 1):
    print(visited[_])