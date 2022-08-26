import sys

input = sys.stdin.readline

hh, mm = map(int, input().split())
time = int(input())

time_table = [0, 0]

time_table[0] = hh
time_table[1] = mm + time

time_table[1] = (mm + time) % 60
cnt_hh = (mm + time) // 60

time_table[0] = (hh + cnt_hh) % 24

print(*time_table)
