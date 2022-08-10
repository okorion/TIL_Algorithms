import sys

a = sys.stdin.readline()
result = set(map(int, sys.stdin.readline().split()))

print(*sorted(result))