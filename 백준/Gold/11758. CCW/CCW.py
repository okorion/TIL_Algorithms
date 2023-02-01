import sys
input = sys.stdin.readline

temp_list = [list(map(int, input().split())) for _ in range(3)]

# print(temp_list)

x1, y1, x2, y2, x3, y3 = temp_list[0][0], temp_list[0][1], temp_list[1][0], temp_list[1][1], temp_list[2][0], temp_list[2][1]

result = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if result > 0:
    print(1)
elif result < 0:
    print(-1)
else:
    print(0)