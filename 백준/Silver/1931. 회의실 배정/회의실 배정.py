import sys

input = sys.stdin.readline

N = int(input())
time = []
temp_list = []

for _ in range(N):
    temp_list.append(list(map(int, input().split())))

temp_list = sorted(temp_list, key=lambda x: (x[1], x[0]))
cnt = 0
last_num = 0

for _ in temp_list:
    if _[0] >= last_num:
        cnt += 1
        last_num = _[1]

print(cnt)
