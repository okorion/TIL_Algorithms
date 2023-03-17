import sys
import heapq
from sys import maxsize

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
visited = [maxsize] * (N + 1)

for _ in range(M):
    A, B, cost = map(int, input().split())

    graph[A].append([B, cost])


start, end = map(int, input().split())

# print(graph)
# print(visited)


def dijkstra(x):
    temp_list = []
    heapq.heappush(temp_list, [x, 0])
    visited[x] = 0

    while temp_list:
        tmp, distance = heapq.heappop(temp_list)

        if visited[tmp] < distance:
            continue

        for b, c in graph[tmp]:
            new = c + distance

            if visited[b] > new:
                heapq.heappush(temp_list, [b, new])
                visited[b] = new


dijkstra(start)
print(visited[end])
