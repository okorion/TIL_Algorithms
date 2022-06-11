import sys

N = int(sys.stdin.readline())
temp_list = list(map(int, sys.stdin.readline().split()))
temp_num = [0] * 1001

empty_list = []
temp_sum = 0

for _ in temp_list:
    temp_num[_] += 1

for __ in range(1001):
    if temp_num[__] == 1:
        empty_list.append(__)
    elif temp_num[__] > 1:
        for ___ in range(temp_num[__]):
            empty_list.append(__)

for ____ in range(N, 0, -1):
    temp_sum += empty_list[N-____] * ____

print(temp_sum)
