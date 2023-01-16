import sys

input = sys.stdin.readline

N = int(input())
val_list = list(map(int, input().split()))
val_list.sort()

target = 1

for _ in val_list:
    if target < _:
        break

    target += _

print(target)
