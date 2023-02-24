import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]
house = []
live_chick = []
result = float('inf')

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append([i, j])
        elif matrix[i][j] == 2:
            live_chick.append([i, j])

for comb in combinations(live_chick, M):
    distance = 0
    for a, b in house:
        dist = float('inf')
        for c, d in comb:
            dist = min(abs(a-c) + abs(b-d), dist)
        distance += dist
    result = min(result, distance)

print(result)
