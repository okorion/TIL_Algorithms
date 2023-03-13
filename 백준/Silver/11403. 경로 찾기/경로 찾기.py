import sys
input = sys.stdin.readline

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

# print(matrix)

for mid in range(N):
    for start in range(N):
        for end in range(N):
            if matrix[start][mid] == 1 and matrix[mid][end]:
                matrix[start][end] = 1

for _ in matrix:
    print(*_)