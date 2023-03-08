import sys
input = sys.stdin.readline

N = int(input())

temp_list = list(map(int, input().split()))
result = [-1] * N
stack = []

# print(temp_list)

for idx, val in enumerate(temp_list):
    while stack and temp_list[stack[-1]] < temp_list[idx]:
        result[stack.pop()] = temp_list[idx]
    stack.append(idx)

print(*result)
