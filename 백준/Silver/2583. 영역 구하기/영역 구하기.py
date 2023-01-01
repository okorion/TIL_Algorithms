from collections import deque

M, N, K = map(int, input().split())

# print(M, N, K)

visited_matrix = [[0 for i in range(N+1)] for j in range(M+1)]

# Input을 통해 직사각형 상태 그리기
for _ in range(K):
    a, b, c, d = map(int, input().split())
    for y in range(M-d, M-b):
        for x in range(a, c):
            visited_matrix[y][x] += 1
    # visited_matrix[M-d:M-b-1][a:c-1] += 1

# print(visited_matrix)

result_cnt = 0
result_list = []

temp_a = [1, 0, -1, 0]   # 우하좌상
temp_b = [0, 1, 0, -1]

temp_deque = deque()
temp_num = 0

for i in range(M+1):          # M = 5, N = 7
    for j in range(N+1):
        if visited_matrix[i][j] == 0 and i < M and j < N:
            temp_deque.append([i, j])
            temp_num += 1
            visited_matrix[i][j] += 1

            while temp_deque:
                y, x = temp_deque.popleft()

                for _ in range(4):
                    if 0 <= y + temp_a[_] < M and 0 <= x + temp_b[_] < N:
                        if visited_matrix[y+temp_a[_]][x+temp_b[_]] == 0:
                            temp_num += 1
                            visited_matrix[y+temp_a[_]][x+temp_b[_]] += 1
                            temp_deque.append([y+temp_a[_], x+temp_b[_]])

            result_cnt += 1
            result_list.append(temp_num)
            temp_num = 0

# print(result_cnt, result_list)
# print(visited_matrix)
print(result_cnt)
print(*sorted(result_list))