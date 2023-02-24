import sys
input = sys.stdin.readline

temp_list = list(map(int, input().split()))

print(sorted(temp_list)[1])
