import sys
import heapq
INF = int(1e9)

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

temp_graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    u, v, w = map(int, input().split())
    temp_graph[u].append([v, w])


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))     # 0-> 가중치, start-> 시작 노드
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if dist > distance[now]:
            continue

        for _ in temp_graph[now]:
            cost = dist + _[1]

            if cost < distance[_[0]]:
                distance[_[0]] = cost
                heapq.heappush(q, (cost, _[0]))


dijkstra(K)

for _ in range(1, V+1):
    if distance[_] == INF:
        print("INF")
    else:
        print(distance[_])

