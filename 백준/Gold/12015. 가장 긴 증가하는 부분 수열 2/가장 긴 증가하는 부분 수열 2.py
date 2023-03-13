import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))

# print(temp_list)
temp = []

for idx, val in enumerate(temp_list):
    if temp and val > temp[-1]:
        temp.append(val)
    else:
        if not temp:
            temp.append(val)
        else:
            # print(bisect_left(temp, val), temp, val)
            temp[bisect_left(temp, val)] = val

print(len(temp))
