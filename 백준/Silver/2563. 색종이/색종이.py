import sys
input = sys.stdin.readline

N = int(input())

matrix = [[0] * 101 for _ in range(101)]
temp_list = [list(map(int, input().split())) for _ in range(N)]


for x, y in temp_list:
    for a in range(x, x+10):
        for b in range(y, y+10):
            matrix[a][b] = 1

result = 0

for _ in matrix:
    result += _.count(1)

print(result)
