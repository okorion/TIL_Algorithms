import sys
input = sys.stdin.readline

N, K = map(int, input().split())

num = list(input())
stack = []
temp = K

for _ in range(N):
    while stack and stack[-1] < num[_] and temp > 0:
        stack.pop()
        temp -= 1
    stack.append(num[_])

print(''.join(stack[:N-K]))
