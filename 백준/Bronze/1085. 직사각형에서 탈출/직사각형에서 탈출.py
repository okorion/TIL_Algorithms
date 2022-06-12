import sys

x, y, w, h = list(map(int, sys.stdin.readline().split()))

minx_table = [x, w-x]
miny_table = [y, h-y]

result_table = minx_table + miny_table

print(min(result_table))
