import sys

N = int(sys.stdin.readline())
temp_list = []

for _ in range(N):
    temp_list.append(list(map(int, sys.stdin.readline().split())))

result_list = sorted(temp_list) + [0]


for _ in range(N):
    print(result_list[_][0], result_list[_][1])