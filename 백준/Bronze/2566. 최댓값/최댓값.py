import sys
input = sys.stdin.readline

matrix = []

result = -float("inf")
tmp = []

for _ in range(9):
    matrix.append(list(map(int, input().split())))

for x in range(9):
    for y in range(9):
        if matrix[x][y] > result:
            result = max(result, matrix[x][y])
            tmp.append(x)
            tmp.append(y)

print(result)
print(f'{tmp[-2] + 1} {tmp[-1] + 1}')
