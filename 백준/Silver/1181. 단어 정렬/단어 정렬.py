import sys

T = int(sys.stdin.readline())

temp_list = []

for testcase in range(T):
    a = str(sys.stdin.readline().rstrip())
    temp_list.append(a)

temp_list = list(set(temp_list))
temp_list.sort()
temp_list.sort(key=len)

for _ in temp_list:
    print(_)
