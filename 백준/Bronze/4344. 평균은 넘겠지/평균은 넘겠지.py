N = int(input())

for _ in range(N):
    temp_list = list(map(int, input().split()))
    temp_list2 = temp_list[1:]

    ratio_num = 0

    if temp_list[0] == 1:
        print("0.000%")
    else:
        for a in temp_list2:
            if a > sum(temp_list2)/int(temp_list[0]):
                ratio_num += 1

        result = ratio_num/int(temp_list[0]) * 100

        print(f"{round(result, 3) :.3f}%")