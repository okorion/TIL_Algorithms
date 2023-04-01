import sys
from collections import deque

input = sys.stdin.readline

col, row = map(int, input().split())
cheese_matrix = [list(map(int, input().split())) for _ in range(col)]


def check_outside(matrix):  # 바깥쪽 0을 2로 전환하기 (내부 공기는 녹는 데 영향이 없으므로)
    for c in range(col):  # 바깥쪽 2를 0으로 재갱신
        for r in range(row):
            if matrix[c][r] == 2:
                matrix[c][r] = 0

    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    queue = deque()
    queue.append([0, 0])
    matrix[0][0] = 2

    while queue:
        x, y = queue.popleft()

        for _ in range(4):
            nx = x + dx[_]
            ny = y + dy[_]

            if 0 <= nx < col and 0 <= ny < row:
                if matrix[nx][ny] == 0:
                    matrix[nx][ny] = 2
                    queue.append([nx, ny])


def melt_hour(matrix):  # 한 시간 흘러 치즈가 녹는 함수
    tmp_col = len(matrix)
    tmp_row = len(matrix[0])
    dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
    flag = [[0] * tmp_row for _ in range(tmp_col)]  # 한 번에 지우기 위해 빈 행렬 flag 생성

    for c in range(tmp_col):
        for r in range(tmp_row):
            if matrix[c][r] == 1:
                for _ in range(4):
                    if 0 <= c + dx[_] < col and 0 <= r + dy[_] < row:
                        if matrix[c + dx[_]][r + dy[_]] == 2:  # 치즈 조각의 상하좌우 중에 2가 있으면 flag에 1 체크
                            flag[c][r] = 1

    for c in range(tmp_col):
        for r in range(tmp_row):
            if flag[c][r] == 1:
                matrix[c][r] = 0

    return


def check_cheese(matrix):  # 치즈가 놓여 있는 칸의 개수 체크
    tmp_col = len(matrix)
    tmp_row = len(matrix[0])
    cnt = 0

    for c in range(tmp_col):
        for r in range(tmp_row):
            if matrix[c][r] == 1:
                cnt += 1

    return cnt


# print(cheese_matrix)

hour = 0
before_cheese_zero = []

while True:
    result = check_cheese(cheese_matrix)
    before_cheese_zero.append(result)
    check_outside(cheese_matrix)
    # print(cheese_matrix)
    melt_hour(cheese_matrix)
    hour += 1

    if check_cheese(cheese_matrix) == 0:
        print(hour)
        print(before_cheese_zero[-1])
        break
