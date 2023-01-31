import sys
import heapq

input = sys.stdin.readline

N = int(input())
h = []

for _ in range(N):
    temp = int(input())

    if temp == 0:
        if len(h) == 0:
            print(0)
        else:
            result = heapq.heappop(h)[1]
            print(result)
    elif temp != 0:
        heapq.heappush(h, (-temp, temp))

