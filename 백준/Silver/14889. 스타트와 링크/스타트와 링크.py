import sys
import itertools

input = sys.stdin.readline

N = int(input())

temp_matrix = []
temp_list = []
temp_list2 = []

target_list = list(range(1, N+1))

for _ in range(N):
    temp_matrix.append(list(map(int, input().split())))

nPr = itertools.combinations(target_list, int(N/2))

for _ in nPr:
    temp_nPr = itertools.combinations(_, 2)
    for a, b in temp_nPr:
        temp_list.append(temp_matrix[a-1][b-1] + temp_matrix[b-1][a-1])

cnt = 0
temp_num = 0
new_temp_list = []

# print(temp_list)

for _ in temp_list:
    temp_num += _
    cnt += 1
    if cnt == sum(range(int(N/2))):
        cnt = 0
        new_temp_list.append(temp_num)
        temp_num = 0

for _ in range(int(len(new_temp_list)/2)):
    temp_list2.append(abs(new_temp_list[_] - new_temp_list[-1-_]))

# print(new_temp_list)
print(min(temp_list2))
