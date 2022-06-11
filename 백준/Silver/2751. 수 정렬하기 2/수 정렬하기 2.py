import sys

T = int(sys.stdin.readline())
temp = [0] * 2000001


for _ in range(T):
    temp[1000000 + int(sys.stdin.readline())] += 1

for __ in range(0, 2000001):
    if temp[__] == 1:
        print(__-1000000)

    else:
        pass