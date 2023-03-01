import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N):
    temp_list = list(input().rstrip())

    print(temp_list[0] + temp_list[-1])
