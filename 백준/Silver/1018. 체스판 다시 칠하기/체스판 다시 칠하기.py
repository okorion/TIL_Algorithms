import sys

N, M = list(map(int, sys.stdin.readline().split()))

new_matrix = []

for _ in range(N):
    new_matrix.append(list(sys.stdin.readline()[:-1:]) + [0])

new_matrix = new_matrix + [[0]*M]

A_matrix = [[0] * 9 for _ in range(9)]
B_matrix = [[0] * 9 for _ in range(9)]

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            A_matrix[i][j] = 'W'
        else:
            A_matrix[i][j] = 'B'

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            B_matrix[i][j] = 'B'
        else:
            B_matrix[i][j] = 'W'

A_list = []
B_list = []

for x in range(0, (M-8)+1):          # 0 1 2 3 4 5
    for y in range(0, (N-8)+1):      # 0 1 2
        tmp_num = 0
        cnt_A = 0
        cnt_B = 0

        if tmp_num != 64:
            for b in range(8):
                for a in range(8):
                    if new_matrix[a + y][b + x] == A_matrix[a][b]:
                        cnt_A += 1

            for b in range(8):
                for a in range(8):
                    if new_matrix[a + y][b + x] == B_matrix[a][b]:
                        cnt_B += 1
                    tmp_num += 1
        elif tmp_num == 64:
            cnt_A = 0
            cnt_B = 0
            tmp_num = 0

        A_list.append(cnt_A)
        B_list.append(cnt_B)

#         print(cnt_A, cnt_B, tmp_num)
# print(A_list, B_list)
# print(new_matrix)
# print(A_matrix)
# print(B_matrix)

result = min(A_list + B_list)
print(result)
