import sys

input = sys.stdin.readline

a, b = map(int, input().split())
temp_min = 0
temp_max = 0

for _ in range(1, min(a, b)+1):
    if a % _ == 0 and b % _ == 0:
        temp_min = _

print(temp_min)
print(int(a/temp_min * b/temp_min * temp_min))
