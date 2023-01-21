import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

user_list = [[] for _ in range(N+1)]


def bacon(graph, start):
    visited = [0] * (N+1)
    queue = deque()
    queue.append(start)

    visited[start] = 1

    while queue:
        temp = queue.popleft()

        for _ in graph[temp]:
            if visited[_] == 0:
                queue.append(_)
                visited[_] = visited[temp]+1
    # print(visited)
    return sum(visited)


for _ in range(M):
    a, b = map(int, input().split())

    user_list[a].append(b)
    user_list[b].append(a)

# print(user_list)
# print(bacon(user_list, 1))
temp_list = []

for _ in range(1, N+1):
    temp_list.append(bacon(user_list, _))
# print(temp_list)
print(temp_list.index(min(temp_list))+1)
