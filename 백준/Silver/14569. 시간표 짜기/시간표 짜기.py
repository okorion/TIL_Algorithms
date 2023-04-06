import sys

input = sys.stdin.readline

n = int(input())   # 과목 수

subjects = []   # 각 과목의 수업시간을 저장할 리스트

for i in range(n):
    k, *times = map(int, input().split())
    bitmask = 0   # 비트마스킹을 위한 변수

    for t in times:
        # 각 교시에 해당하는 비트를 1로 설정
        bitmask |= (1 << (t - 1))
    subjects.append(bitmask)

m = int(input())   # 학생 수
for i in range(m):
    p, *times = map(int, input().split())
    bitmask = 0   # 비트마스킹을 위한 변수

    for t in times:
        # 각 교시에 해당하는 비트를 1로 설정
        bitmask |= (1 << (t - 1))

# 각 학생이 들을 수 있는 과목의 개수를 구하기
    count = 0
    for j in range(n):
        if bitmask & subjects[j] == subjects[j]:
            count += 1

    print(count)
