import sys

input = sys.stdin.readline

N = int(input())
K = int(input())
temp_list = list(map(int, input().split()))

temp_list.sort()
# print(N, K, temp_list)

new_list = []
if N == 1:
    print(0)
    exit()

for _ in range(N - 1):
    new_list.append((temp_list[_ + 1] - temp_list[_]))

new_list.sort()
# print(new_list)

for _ in range(K - 1):
    new_list[-_ - 1] = 0

print(sum(new_list))
