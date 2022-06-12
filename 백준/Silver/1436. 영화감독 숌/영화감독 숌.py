import sys

T = int(sys.stdin.readline())
cnt = 0

result_list = []

for _ in range(1, 10000001):
    if '666' in str(_):
        cnt += 1
        result_list.append(_)
    elif cnt == 10001:
        break

result_list.sort()
# print(result_list)
print(result_list[T-1])
