import sys
import heapq

input = sys.stdin.readline

N = int(input())

temp_list = []

for _ in range(N):
    s, t = map(int, input().split())

    temp_list.append([s, t])

temp_list.sort(key=lambda x: [x])

# print(temp_list)

hq = []
heapq.heappush(hq, temp_list[0][1])

for _ in range(1, N):
    if temp_list[_][0] < hq[0]:
        heapq.heappush(hq, temp_list[_][1])
    else:
        heapq.heappush(hq, temp_list[_][1])
        heapq.heappop(hq)

print(len(hq))
