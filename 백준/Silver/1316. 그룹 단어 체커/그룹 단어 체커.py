import sys

a = int(sys.stdin.readline())
result_num2 = 0

for _ in range(a):
    temp = sys.stdin.readline()
    temp_list = list(map(str, temp.rstrip("\n")))
    temp_list_set = list(set(temp_list))
    temp_num = len(temp_list_set)
    result_num = 0

    #print(temp, temp_list, temp_list_set, temp_num)

    for i in range(temp_num):
        re_num = temp_list.count(temp_list_set[i])


        if (re_num*temp_list_set[i]) in temp:
            result_num += 1
            #print(re_num*temp_list_set[i], re_num, temp_list_set[i], temp)
            if i == temp_num:
                break
        elif (re_num*temp_list_set[i]) not in temp:
            result_num = -1
            break
    if result_num == -1:
        result_num2 += 0
    else:
        result_num2 += 1


print(result_num2)
