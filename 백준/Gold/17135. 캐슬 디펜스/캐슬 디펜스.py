import sys
import copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M, D = map(int, input().split())
tmp_field = deque(list(map(int, input().split())) for _ in range(N))


def bfs(x, y, count):
    global enemy_dead_count

    dx, dy = [0, -1, 0], [-1, 0, 1]

    queue = deque([(x, y, count)])

    while queue:
        x, y, count = queue.popleft()

        if count == D:
            return

        for d in range(3):
            nx = x + dx[d]
            ny = y + dy[d]

            if 0 <= nx < N and 0 <= ny < M:
                if field[nx][ny] == 1:
                    field[nx][ny] += 1
                    return
                elif field[nx][ny] >= 2:
                    field[nx][ny] += 1
                    return
                queue.append((nx, ny, count + 1))


def attack(archer_location):    # archer_location의 값으로 set을 받음. (0, 1, 2), (0, 1, 3) ~
    global enemy_dead_count

    archer_list = [0] * M

    # print("궁수 좌표", archer_xy)

    field.append(archer_list)    # 적 제거 시작

    for _ in archer_location:
        archer_list[_] = -1
        bfs(N, _, 0)

    for p in range(N):
        for q in range(M):
            if field[p][q] >= 2:
                enemy_dead_count += 1
                field[p][q] = 0

    # print(field, enemy_dead_count)

    field.pop()

    # print(field, enemy_dead_count)
    # print("궁수 위치 담긴 리스트", archer_list)
    # print("field 임시 확장", field)
    # print("field 정리", field)


def move():
    field.extendleft([[0] * M])
    field.pop()


answer = 0

for _ in combinations(range(M), 3):
    field = copy.deepcopy(tmp_field)
    # print("궁수 위치", _)
    enemy_dead_count = 0

    for n in range(N):
        attack(_)    # 마지막 행의 적 삭제
        move()    # 궁수 사격 이후 적들의 전진

    answer = max(answer, enemy_dead_count)

# print("제거한 적의 최대 수", answer)
print(answer)
