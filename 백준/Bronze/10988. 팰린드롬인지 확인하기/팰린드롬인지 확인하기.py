import sys

input = sys.stdin.readline

tmp = list(input().rstrip())

if tmp == list(reversed(tmp)):
    print(1)
else:
    print(0)
