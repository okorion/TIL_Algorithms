import sys
input = sys.stdin.readline

temp_list = [list(map(int, input().split())) for _ in range(2)]

x1, y1, x2, y2 = temp_list[0][0], temp_list[0][1], temp_list[0][2], temp_list[0][3]
x3, y3, x4, y4 = temp_list[1][0], temp_list[1][1], temp_list[1][2], temp_list[1][3]

result1 = (x2 * y3 + x3 * y1 + x1 * y2) - (x2 * y1 + x3 * y2 + x1 * y3)  # 123
result2 = (x2 * y4 + x4 * y1 + x1 * y2) - (x2 * y1 + x4 * y2 + x1 * y4)  # 124

result3 = (x2 * y3 + x3 * y4 + x4 * y2) - (x2 * y4 + x3 * y2 + x4 * y3)  # 234
result4 = (x1 * y3 + x3 * y4 + x4 * y1) - (x3 * y1 + x4 * y3 + x1 * y4)  # 134


if result1 * result2 < 0 and result3 * result4 < 0:
    print(1)
else:
    # print(result1, result2, result3, result4)
    print(0)

# print(temp_list)