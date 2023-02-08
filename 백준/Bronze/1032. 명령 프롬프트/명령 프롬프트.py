import sys

input = sys.stdin.readline

N = int(input())
result_list = []

result_list = list(input().rstrip())
# print(len(result_list))
for t in range(N-1):
    temp_list = list(input().rstrip())
    for _ in range(len(result_list)):
        if result_list[_] != temp_list[_]:
            result_list[_] = '?'
        else:
            pass

print(''.join(result_list))
