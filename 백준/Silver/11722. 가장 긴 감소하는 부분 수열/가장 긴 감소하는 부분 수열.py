import sys
from bisect import bisect_left

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
temp_list = temp_list[::-1]

stack = []
result_list = []

for temp in temp_list:
    if not stack or temp > stack[-1]:
        stack.append(temp)
        result_list.append([bisect_left(stack, temp), temp])

    else:
        stack[bisect_left(stack, temp)] = temp
        result_list.append([bisect_left(stack, temp), temp])

# print(stack, result_list)
print(len(stack))
