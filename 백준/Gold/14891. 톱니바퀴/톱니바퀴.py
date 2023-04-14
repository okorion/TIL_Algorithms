import sys
from collections import deque

input = sys.stdin.readline


def right_rotate(x, direct):
    if x > 4 or gear_dict[x - 1][2] == gear_dict[x][6]:
        return

    if gear_dict[x - 1][2] != gear_dict[x][6]:
        right_rotate(x + 1, -direct)
        gear_dict[x].rotate(direct)


def left_rotate(x, direct):
    if x < 1 or gear_dict[x][2] == gear_dict[x + 1][6]:
        return

    if gear_dict[x][2] != gear_dict[x + 1][6]:
        left_rotate(x - 1, -direct)
        gear_dict[x].rotate(direct)


gear_dict = {}

for _ in range(1, 5):
    gear_dict[_] = deque((map(int, input().rstrip())))

N = int(input())

for _ in range(N):
    a, b = map(int, input().split())

    right_rotate(a + 1, -b)
    left_rotate(a - 1, -b)
    gear_dict[a].rotate(b)

result = 0

for _ in range(1, 5):
    result += gear_dict[_][0] * (2 ** (_ - 1))

print(result)
