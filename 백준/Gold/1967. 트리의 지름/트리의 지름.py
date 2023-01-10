import sys
sys.setrecursionlimit(10 ** 9)

input = sys.stdin.readline

N = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])    # b는 도착 노드, c는 가중치(거리)
    graph[b].append([a, c])


def dfs(k, value):    # 시작 노드 k, 가중치 value
    for x, y in graph[k]:
        if visited[x] == -1:
            visited[x] = y + value
            dfs(x, y + value)


visited = [-1] * (N+1)
visited[1] = 0
dfs(1, 0)

start = visited.index(max(visited))

visited = [-1] * (N+1)
visited[start] = 0
dfs(start, 0)

print(max(visited))
