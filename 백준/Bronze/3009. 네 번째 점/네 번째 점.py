import sys

input = sys.stdin.readline

temp_x = []
temp_y = []

x = 0
y = 0

for _ in range(3):
    x, y = map(int, input().split())
    temp_x.append(x)
    temp_y.append(y)

for _ in temp_x:
    if temp_x.count(_) == 1:
        x = _

for _ in temp_y:
    if temp_y.count(_) == 1:
        y = _

print(x, y)