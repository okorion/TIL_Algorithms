import sys

input = sys.stdin.readline

N = int(input())

for n in range(N):
    temp_list = input().rstrip().split(' ')
    result = ''
    temp_list = ' '.join(temp_list[::-1])

    print(f'Case #{n + 1}: {temp_list}')
