import sys

input = sys.stdin.readline

a = int(input())

for tc in range(1, 10):
    tc2 = a * tc
    print(f'{a} * {tc} = {tc2}')
