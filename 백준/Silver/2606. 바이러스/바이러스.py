from collections import deque

N = int(input())
num = int(input())
temp_graph = [list() for i in range(N+1)]
visited_list = [0] * (N+1)

for _ in range(num):
    a, b = map(int, input().split())
    temp_graph[a-1] += [b]
    temp_graph[b-1] += [a]

# print(temp_graph)

dQ = deque([0])

# print(dQ)

while dQ:
    k = dQ.popleft()
    for _ in temp_graph[k]:
        if visited_list[_-1] == 0:
            visited_list[_-1] = 1
            dQ.append(_-1)

print(sum(visited_list)-1)    # 본인 제외
