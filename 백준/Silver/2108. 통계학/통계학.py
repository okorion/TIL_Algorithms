import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
temp_list = []


def mode(numbers):
    temp = Counter(numbers)
    order = temp.most_common()
    maximum = order[0][1]
    result_list = []

    order.sort()
    # print(order)
    for _ in order:
        if _[1] == maximum:
            result_list.append(_[0])

    if len(result_list) == 1:
        return result_list[0]
    else:
        return result_list[1]


for _ in range(N):
    temp_list.append(int(input()))

print(int(round((sum(temp_list) / len(temp_list)), 0)))
print(int(sorted(temp_list)[N // 2]))
print(mode(temp_list))
print(max(temp_list) - min(temp_list))