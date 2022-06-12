import sys

N = int(sys.stdin.readline())


def recursion(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return recursion(n-1) + recursion(n-2)


print(recursion(N))
