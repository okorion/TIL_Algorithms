import sys
from collections import deque
input = sys.stdin.readline


def direct(c, d):
    if d == 'D':
        c = (c + 1) % 4
    if d == 'L':
        c = (c - 1) % 4

    return c


def start():
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    direction = 1
    x, y = 0, 0
    snake.append([y, x])
    matrix[y][x] = 2
    time = 1

    while True:
        x = x + dx[direction]
        y = y + dy[direction]

        if 0 <= x < N and 0 <= y < N and matrix[y][x] != 2:
            if not matrix[y][x] == 1:    #뱀이 일반 바닥에 위치
                ny, nx = snake.popleft()
                matrix[ny][nx] = 0
            matrix[y][x] = 2
            snake.append([y, x])

            if time in times.keys():
                direction = direct(direction, times[time])
            time += 1
        else:
            return time


N = int(input())
K = int(input())

matrix = [[0] * N for _ in range(N)]
apple_list = [list(map(int, input().split())) for _ in range(K)]

for a, b in apple_list:
    matrix[a-1][b-1] = 1

L = int(input())
move = [list(input().split()) for _ in range(L)]
snake = deque()
times = {}

for num, d in move:
    times[int(num)] = d

print(start())
