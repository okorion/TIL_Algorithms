import sys

input = sys.stdin.readline

N = int(input())

distance_list = list(map(int, input().split()))
oil_bank = list(map(int, input().split()))[:-1]
result_num = 0
m = 10000000000

for _ in range(N-1):
    if oil_bank[_] < m:
        m = oil_bank[_]
    result_num += distance_list[_] * m

# while len(distance_list) != 0:
#     a = oil_bank.index(min(oil_bank))
#     result_num += sum(distance_list[a:]) * oil_bank[a]
#
#     distance_list = distance_list[:a]
#     oil_bank = oil_bank[:a]

print(result_num)
