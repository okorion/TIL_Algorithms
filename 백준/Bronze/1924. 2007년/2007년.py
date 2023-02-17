import sys
input = sys.stdin.readline

calendar = list(map(int, input().split()))

day_2007 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_result = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']

mon, day = calendar

# print(mon, day)

temp_day = 0

if mon > 1:
    temp_day += sum(day_2007[0:mon-1])

temp_day += day

print(day_result[temp_day % 7])
