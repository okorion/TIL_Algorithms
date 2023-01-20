import sys

input = sys.stdin.readline

N, M = map(int, input().split())

A_matrix = []
B_matrix = []

for _ in range(N):
    A_matrix.append(list(map(int, input().strip())))

for _ in range(N):
    B_matrix.append(list(map(int, input().strip())))

# print(A_matrix)
# print(B_matrix)


def change(a, b, matrix):
    for x in range(3):
        for y in range(3):
            if matrix[a + x][b + y] == 1:
                matrix[a + x][b + y] = 0
            elif matrix[a + x][b + y] == 0:
                matrix[a + x][b + y] = 1


result = 0

for i in range(N-2):
    for j in range(M-2):
        if A_matrix[i][j] != B_matrix[i][j]:
            change(i, j, A_matrix)
            result += 1

if A_matrix == B_matrix:
    print(result)
else:
    print(-1)
    