import sys
from itertools import combinations


input = sys.stdin.readline

temp_list = []

for _ in range(9):
    temp_list.append(int(input()))

for a in combinations(temp_list, 7):
    if sum(a) == 100:
        for result in sorted(list(a)):
            print(result)
        break