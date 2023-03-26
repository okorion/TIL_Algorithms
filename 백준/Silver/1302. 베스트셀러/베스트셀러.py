import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
temp_list = []

for _ in range(N):
    temp_list.append(input().rstrip())

temp_list.sort()
temp_list = Counter(temp_list)

# print(temp_list)
print(temp_list.most_common()[0][0])
