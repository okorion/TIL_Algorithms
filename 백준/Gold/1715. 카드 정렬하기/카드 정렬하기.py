import sys
import heapq

input = sys.stdin.readline

N = int(input())
queue = []

for _ in range(N):
    heapq.heappush(queue, int(input()))

result = 0

while len(queue) > 1:
    val = heapq.heappop(queue) + heapq.heappop(queue)
    result += val
    heapq.heappush(queue, val)

print(result)
