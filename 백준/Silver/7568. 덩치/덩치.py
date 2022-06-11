import sys

T = int(sys.stdin.readline())
temp_array = []

for _ in range(T):
    temp_array.append(list(map(int, sys.stdin.readline().split())))

# print(temp_array)

for i in range(T):
    for j in range(T):
        if i != j:
            if temp_array[i][0] < temp_array[j][0] and temp_array[i][1] < temp_array[j][1]:
                temp_array[i].append(7777)


# print(temp_array)

temp_list = []

for k in temp_array:
    temp_result_len = len(k)
    temp_list.append(temp_result_len)

# print(temp_list)
new_list = []

for __ in temp_array:
    new_list.append(len(__)-1)

print(*new_list)

# result_list = [1] * (len(temp_list)+1)
#
# for a in range(len(temp_list)):    # [2, 4, 6, 3, 3, 2] => 1 5 6 3 3 1  의 방식(리스트 중 자신보다 큰 수+1)으로 순위 조절
#     for b in range(len(temp_list)):
#         if temp_list[a] > temp_list[b]:
#             result_list[a] += 1
#
# del result_list[-1]
#
# print(*result_list)
