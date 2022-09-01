import sys

input = sys.stdin.readline

hh, mm = map(int, input().split())

if mm < 45:
    if hh >= 1:
        pre_hh = hh - 1
        pre_mm = 60 + mm - 45
    else:
        pre_hh = 23
        pre_mm = 60 + mm - 45

else:
    pre_hh = hh
    pre_mm = mm - 45

print(pre_hh, pre_mm)
