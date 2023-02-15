import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

num = A * B * C

temp_list = [0 for _ in range(10)]

for _ in list(str(num)):
    for temp in range(10):
        # print(temp, int(_))
        if temp == int(_):
            temp_list[int(_)] += 1

for _ in temp_list:
    print(_)
