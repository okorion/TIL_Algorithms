import sys

input = sys.stdin.readline

N = int(input())

for _ in range(N // 5, -1, -1):
    N -= _ * 5
    if not N % 2:
        print(_ + N // 2)
        break
    N += _ * 5
    
    if _ == 0 and N % 2 != 0:
        print(-1)
        break
