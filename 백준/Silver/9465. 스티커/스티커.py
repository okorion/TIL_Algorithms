import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    matrix = [list(map(int, input().split()))] + [list(map(int, input().split()))]

    for i in range(1, N):
        if i == 1:
            matrix[0][i] += matrix[1][i - 1]
            matrix[1][i] += matrix[0][i - 1]
        else:
            matrix[0][i] += max(matrix[1][i-1], matrix[1][i-2])
            matrix[1][i] += max(matrix[0][i-1], matrix[0][i-2])

    print(max(matrix[0][N-1], matrix[1][N-1]))
