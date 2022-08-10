import sys

temp_list = []

N = int(sys.stdin.readline())

for n in range(N):
    temp_list.append(list(map(int, sys.stdin.readline().split())))

result_list = sorted(temp_list, key=lambda x: (x[1], x[0]))

for r in range(N):
    print(*result_list[r])
    