import sys

input = sys.stdin.readline


def is_good_student(matrix, i, j, temp_list):   #[idx]
    empty_cnt = 0
    cnt = 0
    
    a = [-1, 0, 0, 1]    #상좌우하
    b = [0, -1, 1, 0]
    
    if i >= 1 and j >= 1:
        for _ in range(4):
            if matrix[i+a[_]][j+b[_]] == 0:
                empty_cnt += 1
            elif matrix[i+a[_]][j+b[_]] in temp_list:
                cnt += 1
    elif i >= 1 and j == 0:
        for _ in [0, 2, 3]:
            if matrix[i+a[_]][j+b[_]] == 0:
                empty_cnt += 1
            elif matrix[i+a[_]][j+b[_]] in temp_list:
                cnt += 1
    elif i == 0 and j >= 1:
        for _ in [1, 2, 3]:
            if matrix[i+a[_]][j+b[_]] == 0:
                empty_cnt += 1      
            elif matrix[i+a[_]][j+b[_]] in temp_list:
                cnt += 1
    elif i == 0 and j == 0:
        for _ in [2, 3]:
            if matrix[i+a[_]][j+b[_]] == 0:
                empty_cnt += 1       
            elif matrix[i+a[_]][j+b[_]] in temp_list:
                cnt += 1            
                         
    return (cnt, empty_cnt)


N = int(input())

result_matrix = [[0]*N+[-1] for _ in range(N)] + [[-1]*(N+1)]


temp_list = [[0]] * (N**2+1)
idx_array = []

for _ in range(N**2):
    idx, a, b, c, d = list(map(int, input().split()))
    temp_list[idx] = [a, b, c, d]
    idx_array.append(idx)
    
for idx in idx_array:
    dd = temp_list[idx]
    temp_cnt = 0
    temp_i = 0
    temp_j = 0
    temp_empty = 0
    for col in range(N-1, -1, -1):
        for row in range(N-1, -1, -1):
            if result_matrix[col][row] == 0:
                aa = is_good_student(result_matrix, col, row, dd)
                if aa[0] > temp_cnt:
                    temp_cnt = aa[0]
                    temp_i = col
                    temp_j = row
                    temp_empty = aa[1]
                elif aa[0] == temp_cnt:   #aa[0]은 cnt, aa[1]은 empty_cnt
                    if aa[1] >= temp_empty:
                        temp_i = col
                        temp_j = row
                        temp_empty = aa[1]
    result_matrix[temp_i][temp_j] = idx
    
result_sum = 0
    
for i in range(N):
    for j in range(N):
        a = is_good_student(result_matrix, i, j, temp_list[result_matrix[i][j]])
        if a[0] == 0:
            result_sum += 0
        elif a[0] == 1:
            result_sum += 1
        elif a[0] == 2:
            result_sum += 10
        elif a[0] == 3:
            result_sum += 100
        elif a[0] == 4:
            result_sum += 1000

print(result_sum)
