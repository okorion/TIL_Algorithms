import sys
input = sys.stdin.readline

temp = int(input())

N_matrix = [[1] * 10 for _ in range(temp)]

for i in range(1, len(N_matrix)):
    for j in range(1, 10):
        N_matrix[i][j] = N_matrix[i-1][j] + N_matrix[i][j-1]

print(sum(N_matrix[temp-1]) % 10007)
