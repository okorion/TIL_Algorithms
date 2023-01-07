temp_list = list(map(int, input().strip().split()))
is_mixed = False

for _ in range(len(temp_list)):
    if _ != 0:
        if temp_list[_] - temp_list[_-1] == 1:
            if _ == len(temp_list) - 1:
                print('ascending')
        elif temp_list[_] - temp_list[_-1] == -1:
            if _ == len(temp_list) - 1:
                print('descending')
        else:
            print('mixed')
            break
