import sys
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())
    tmp = [a, b, c]

    tmp.sort()

    if a == 0 and b == 0 and c == 0:
        break

    if tmp[0] ** 2 + tmp[1] ** 2 == tmp[2] ** 2:
        print('right')
    else:
        print('wrong')
