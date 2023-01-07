N = int(input())
temp_list = []

for _ in range(N):
    temp_list.append(list(map(str, input().split())))

# print(temp_list)
for n in range(len(temp_list)):
    temp_list_new = []
    for m in range(len(temp_list[n][1])):
        temp_list_new += temp_list[n][1][m] * int(temp_list[n][0])
    print(''.join(temp_list_new))
