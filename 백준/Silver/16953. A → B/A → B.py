import sys

input = sys.stdin.readline

A, B = map(int, input().split())
count = 1

while True:
    if B % 2 == 0:    #B가 짝수일 때
        B = B / 2
        count += 1
    elif B % 10 == 1:    #B가 1로 끝날 때
        B = int(B/10)
        count += 1
    else:
        count = -1
        break

    if A == B:
        break

    if A > B:
        count = -1
        break

print(count)
