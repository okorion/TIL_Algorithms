import sys

input = sys.stdin.readline

n, k = map(int, input().split())

skills = []
for i in range(n):
    a, b, c = map(int, input().split())
    skills.append((a, b, c))

# 가능한 모든 두 가지 역량 조합을 리스트에 저장
pairs = []
for i in range(3):
    for j in range(i+1, 3):
        pairs.append((i, j))

# 두 가지 역량 합이 최대가 되는 조합 찾기
max_sum = 0
for pair in pairs:
    temp = [skills[i][pair[0]] + skills[i][pair[1]] for i in range(n)]
    temp = sorted(temp, reverse=True)[:k] # 내림차순 정렬 후 k개만 선택
    max_sum = max(max_sum, sum(temp))

print(max_sum)
