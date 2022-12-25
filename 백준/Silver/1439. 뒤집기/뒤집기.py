temp_list = list(input())
result_list = []
temp = -1

for _ in temp_list:
    if temp != _:
        result_list.append(_)
        temp = _
    else:
        pass

num_0 = result_list.count('0')
num_1 = result_list.count('1')

print(min(num_0, num_1))
