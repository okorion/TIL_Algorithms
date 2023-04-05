import sys
input = sys.stdin.readline

tmp = list(input().rstrip())
result = ['U', 'C', 'P', 'C']
visited = [0] * 4

i = 0

for _ in tmp:
    if _ == result[i]:
        i += 1
    if i == 4:
        print('I love UCPC')
        quit(0)

print('I hate UCPC')

