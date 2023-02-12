import sys
import re
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    a = input().strip()
    temp = re.compile('(100+1+|01)+')

    if temp.fullmatch(a):
        print('YES')
    else:
        print('NO')
