import sys

input = sys.stdin.readline

n = int(input())  # 탑의 개수
heights = list(map(int, input().split()))  # 탑의 높이

stack = []  # 스택을 이용하여 수신한 탑의 번호를 저장할 리스트
for i in range(n):
    # print('stack=', stack, 'height=', heights)
    while stack:
        # 스택에 있는 탑 중에서 현재 탑의 높이보다 높이가 낮은 탑은 수신할 수 없으므로 제거한다.
        if heights[stack[-1]] < heights[i]:
            stack.pop()
        else:
            break
    if stack:
        # 스택에 있는 탑 중에서 가장 오른쪽에 있는 탑이 수신할 수 있다.
        print(stack[-1] + 1, end=' ')
    else:
        print(0, end=' ')
    stack.append(i)
