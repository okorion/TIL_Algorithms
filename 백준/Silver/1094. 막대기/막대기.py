import sys
input = sys.stdin.readline

X = int(input())

answer = 0   # 16, 4, 2, 1
tmp = 64
result = 0

while True:
    answer = X // tmp
    if answer:
        X -= answer * tmp
        result += 1
    tmp = tmp // 2
    if X == 0:
        break

print(result)
