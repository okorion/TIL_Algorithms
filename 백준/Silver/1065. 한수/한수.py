import sys

input = sys.stdin.readline

N = int(input())
temp_list = []
result_list = []

for _ in range(1, 1001):
    temp_list.append(_)

for _ in range(len(temp_list)):
    if 1 <= temp_list[_] < 10:
        result_list.append(temp_list[_])
    elif 10 <= temp_list[_] < 100:
        result_list.append(temp_list[_])
    elif 100 <= temp_list[_] < 1000:
        if temp_list[_] // 100 - ((temp_list[_]//10)-(temp_list[_] // 100)*10) == (((temp_list[_]//10)-(temp_list[_] // 100)*10)-(temp_list[_]%10)):
            result_list.append(temp_list[_])

cnt = 0

for _ in result_list:
    if _ <= N:
        cnt += 1

print(cnt)
