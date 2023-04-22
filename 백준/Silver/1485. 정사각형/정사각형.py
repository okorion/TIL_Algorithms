import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    tmp = []

    for r in range(4):
        a, b = map(int, input().split())

        tmp.append([a, b])

    # print(tmp)

    tmp.sort()

    # print(tmp)

    flag = True
    # 중점 일치
    if (tmp[0][0] + tmp[3][0]) / 2 == (tmp[1][0] + tmp[2][0]) / 2:
        if (tmp[0][1] + tmp[3][1]) / 2 == (tmp[1][1] + tmp[2][1]) / 2:
            pass
        else:
            flag = False
    else:
        flag = False

    # 대각선 길이 일치
    p = abs(tmp[3][0] - tmp[0][0]) ** 2 + abs(tmp[3][1] - tmp[0][1]) ** 2
    q = abs(tmp[2][0] - tmp[1][0]) ** 2 + abs(tmp[2][1] - tmp[1][1]) ** 2

    if p == q:
        pass
    else:
        flag = False

    # 접한 두 선분 길이 일치
    x = abs(tmp[1][0] - tmp[0][0]) ** 2 + abs(tmp[1][1] - tmp[0][1]) ** 2
    y = abs(tmp[2][0] - tmp[0][0]) ** 2 + abs(tmp[2][1] - tmp[0][1]) ** 2

    if x == y:
        pass
    else:
        flag = False

    print(int(flag))
