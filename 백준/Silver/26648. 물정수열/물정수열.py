import sys
input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(3)]

x = -1    # 증가수열의 가능한 작은 마지막 항. 다음 수열로 값을 넘겨줄 때 x값이 가능한 작은 것이 항상 유리.
flag = True

for _ in range(N):
    a, b, c = matrix[0][_], matrix[1][_], matrix[2][_]

    L_i = min(a, b, c)    # a, b, c 의 세 수 중, 한 수를 바꿔서 만들 수 있는 중위수는 L_i 또는 R_i
    R_i = max(a, b, c)

    if R_i <= x:
        flag = False
        break
    elif x < L_i:
        x = L_i
    elif L_i <= x < R_i:
        x = x + 1

if flag:
    print("YES")
else:
    print("NO")
    