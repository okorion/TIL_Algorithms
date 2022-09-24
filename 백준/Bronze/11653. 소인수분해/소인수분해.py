import sys

input = sys.stdin.readline

N = int(input())

def rec(n):
    if n == 1:
        return
    for _ in range(2, n+1):
        if n % _ == 0:
            print(_)
            rec(n//_)
            break

        
rec(N)
