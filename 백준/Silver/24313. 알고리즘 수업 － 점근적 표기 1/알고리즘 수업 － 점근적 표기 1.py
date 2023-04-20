import sys
input = sys.stdin.readline

a, b = map(int, input().split())

c = int(input())
n = int(input())

tmp = n

if c-a < 0:
    print(0)
elif b <= (c-a) * tmp:
    print(1)
else:
    print(0)