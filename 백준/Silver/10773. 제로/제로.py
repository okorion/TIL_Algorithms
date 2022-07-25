import sys

N = int(sys.stdin.readline().rstrip())

temp_list = []

for num in range(N):
    a = int(input())

    if a != 0:
        temp_list.append(a)
    else:
        temp_list.pop(-1)

print(sum(temp_list))
