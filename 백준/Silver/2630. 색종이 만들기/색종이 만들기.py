import sys

input = sys.stdin.readline

N = int(input())
matrix = []

for _ in range(N):
    matrix.append(list(map(int, input().split())))

cnt_blue = 0
cnt_white = 0


def rec(x, y, n):
    global cnt_white, cnt_blue
    color = matrix[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != matrix[i][j]:
                rec(x, y, n // 2)
                rec(x + n // 2, y, n // 2)
                rec(x, y + n // 2, n // 2)
                rec(x + n // 2, y + n // 2, n // 2)
                return

    if color == 1:
        cnt_blue += 1

    elif color == 0:
        cnt_white += 1


rec(0, 0, N)

print(cnt_white)
print(cnt_blue)
