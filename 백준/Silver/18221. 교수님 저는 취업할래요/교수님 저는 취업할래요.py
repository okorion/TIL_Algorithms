import sys
input = sys.stdin.readline

N = int(input().rstrip())
matrix = [list(map(int, input().split())) for _ in range(N)]

me = []
professor = []
student = []

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 5:
            me.append([i, j])
        elif matrix[i][j] == 2:
            professor.append([i, j])
        elif matrix[i][j] == 1:
            student.append([i, j])

flag = True

if (professor[0][0] - me[0][0]) ** 2 + (professor[0][1] - me[0][1]) ** 2 < 5 ** 2:
    flag = False

cross = 0
for _ in student:
    if min(me[0][0], professor[0][0]) <= _[0] <= max(me[0][0], professor[0][0]):
        if min(me[0][1], professor[0][1]) <= _[1] <= max(me[0][1], professor[0][1]):
            cross += 1

if cross < 3:
    flag = False

print(int(flag))
