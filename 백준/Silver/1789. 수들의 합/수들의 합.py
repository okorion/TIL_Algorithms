import sys

input = sys.stdin.readline

S = int(input())
result = 0
temp = 1

while True:
    if result > S:
        break

    result += temp
    temp += 1

print(temp - 2)
