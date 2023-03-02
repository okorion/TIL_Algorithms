import sys
input = sys.stdin.readline

N, M = map(int, input().split())
matrix = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
answer = []

dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
# print(matrix)
# print(visited)


def bfs(x, y):
    for t in range(1, M):
        flag = True

        for _ in range(4):
            nx = x + dx[_] * t
            ny = y + dy[_] * t

            if 0 <= nx < N and 0 <= ny < M and matrix[nx][ny] == "*":
                pass
            else:
                flag = False
                break

        if flag:
            answer.append([x + 1, y + 1, t])
            # print(answer)

            for _ in range(4):
                nx = x + dx[_] * t
                ny = y + dy[_] * t

                visited[nx][ny] = 0
            visited[x][y] = 0
        else:
            break


for a in range(N):
    for b in range(M):
        if matrix[a][b] == '*':
            visited[a][b] = 1

for a in range(N):
    for b in range(M):
        if matrix[a][b] == '*':
            bfs(a, b)

total = 0

for a in range(N):
    for b in range(M):
        total += visited[a][b]

if total == 0:
    print(len(answer))
    for _ in answer:
        print(*_)
else:
    print(-1)
