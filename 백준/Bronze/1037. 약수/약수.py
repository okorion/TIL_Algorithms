import sys

input = sys.stdin.readline

N = int(input())
temp_list = list(map(int, input().split()))
temp_list.sort()

print(temp_list[0] * temp_list[-1])
