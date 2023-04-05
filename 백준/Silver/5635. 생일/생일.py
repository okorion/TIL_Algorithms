import sys
input = sys.stdin.readline

N = int(input())
temp_list = [input().rstrip().split() for _ in range(N)]

# print(temp_list)
num_list = []

for name, d, m, y in temp_list:
    num_list.append(int(y) * 10000 + int(m) * 100 + int(d))

# print(num_list)
print(temp_list[num_list.index(max(num_list))][0])
print(temp_list[num_list.index(min(num_list))][0])
