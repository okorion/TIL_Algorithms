import sys

input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    temp_list = []

    for n in range(N):
        temp_list.append(list(map(int, input().split())))

    temp_list.sort()

    temp_num = temp_list[0][1]
    result_list = []
    result = 1

    for a, b in temp_list:
        if b < temp_num:
            temp_num = b
            result += 1
    
    print(result)
