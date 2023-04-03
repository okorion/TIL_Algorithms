import sys
input = sys.stdin.readline

time = list(map(int, input().split()))
n = int(input())

# print(time, n)

if n // 3600:
    time[0] += n // 3600
    n = n % 3600

if n // 60:
    time[1] += n // 60
    n = n % 60

time[2] += n

if time[2] >= 60:
    time[2] = time[2] % 60
    time[1] += 1

if time[1] >= 60:
    time[1] = time[1] % 60
    time[0] += 1

if time[0] >= 24:
    time[0] = time[0] % 24

print(*time)
