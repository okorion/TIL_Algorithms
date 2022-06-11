import sys

N, K = map(int, sys.stdin.readline().split())
cnt = 0
temp_list = []

for _ in range(N):
    temp_list.append(int(sys.stdin.readline()))

temp_list = temp_list[::-1]

for __ in temp_list:
    if K >= __:
        cnt += K // __
        K = K % __
    else:
        pass

print(cnt)
