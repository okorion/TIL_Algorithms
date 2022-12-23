import sys

sys.stdin = open("input.txt", 'r')

input = sys.stdin.readline

N = int(input())


def medicine_1(n):
    if n >= 200 or n < 210:
        if 209-n < 8:
            return 209-n+1
        else:
            return 8


def medicine_2(n):
    if n >= 200 or n < 220:
        if 219-n < 4:
            return 219-n+1
        else:
            return 4


def medicine_3(n):
    if n >= 200 or n < 230:
        if 229-n < 2:
            return 229-n+1
        else:
            return 2


def medicine_4(n):
    return 1


result_list = []

result_list.append(medicine_4(N))
result_list.append(medicine_3(N))
result_list.append(medicine_2(N))
result_list.append(medicine_1(N))

print(4-result_list.index(max(result_list)))
