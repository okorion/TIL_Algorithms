import sys

N = int(sys.stdin.readline())
new_list = list(map(int, sys.stdin.readline().split()))
result_list = []

for _ in new_list:
    cnt = 0

    for __ in range(1, _+1):
        if _ % __ == 0:
            cnt += 1

    result_list.append(cnt)

print(result_list.count(2))
