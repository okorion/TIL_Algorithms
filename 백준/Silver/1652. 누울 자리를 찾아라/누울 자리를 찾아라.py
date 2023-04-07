import sys

input = sys.stdin.readline

n = int(input())  # 방의 크기

# 방의 구조를 2차원 배열로 읽어들임
room = []
for i in range(n):
    room.append(input())

# 가로 방향으로 누울 수 있는 자리의 개수
horizontal_count = 0
for i in range(n):
    j = 0
    while j < n:
        if room[i][j] == '.':
            cnt = 0
            while j < n and room[i][j] == '.':
                cnt += 1
                j += 1
            if cnt >= 2:
                horizontal_count += 1
        else:
            j += 1

# 세로 방향으로 누울 수 있는 자리의 개수
vertical_count = 0
for j in range(n):
    i = 0
    while i < n:
        if room[i][j] == '.':
            cnt = 0
            while i < n and room[i][j] == '.':
                cnt += 1
                i += 1
            if cnt >= 2:
                vertical_count += 1
        else:
            i += 1

print(horizontal_count, vertical_count)
