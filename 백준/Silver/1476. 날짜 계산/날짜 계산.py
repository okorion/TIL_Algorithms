import sys

input = sys.stdin.readline

E, S, M = map(int, input().split())
temp_list = [E, S, M]
a, b, c = 1, 1, 1
result_list = []


for plus_year in range(100000):
    if [a, b, c] == [E, S, M]:
        print(plus_year+1)
        break
    else:
        a = a % 15 + 1
        b = b % 28 + 1
        c = c % 19 + 1

