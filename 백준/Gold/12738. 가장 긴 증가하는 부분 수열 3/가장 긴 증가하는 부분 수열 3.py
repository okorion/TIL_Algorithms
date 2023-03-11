import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())

temp_list = list(map(int, input().split()))

# print(temp_list)

tmp = []
result = []

for idx, val in enumerate(temp_list):
    if not tmp or tmp[-1] < val:
        tmp.append(temp_list[idx])
        result.append([bisect_left(tmp, val), val])

    elif tmp[-1] >= val:
        tmp[bisect_left(tmp, val)] = val
        result.append([bisect_left(tmp, val), val])

print(len(tmp))
