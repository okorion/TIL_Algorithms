import sys

input = sys.stdin.readline

temp = list(list(input().strip()) for _ in range(5))

result = ""

for n in range(15):
    for _ in temp:
        if n < len(_):
            result += _[n]

print(result)
