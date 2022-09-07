import sys

input = sys.stdin.readline

cnt = 0
temp_list = []

for _ in range(10):
    temp_list.append((int(input()) % 42))

print(len(set(temp_list)))
