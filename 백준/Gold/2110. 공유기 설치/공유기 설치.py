import sys

input = sys.stdin.readline

N, C = map(int, input().rstrip().split())

router_list = [int(input()) for _ in range(N)]

router_list.sort()

# print(router_list)

answer = 0


def binary_search():
    global answer

    start = 1
    end = router_list[-1] - router_list[0]

    while start <= end:
        mid = (start + end) // 2
        current = router_list[0]
        cnt = 1

        for _ in range(1, len(router_list)):   #mid(공유기 사이 임의 거리) 를 만족하는 공유기 개수 카운트
            if router_list[_] >= current + mid:
                current = router_list[_]
                cnt += 1

        if cnt >= C:   #공유기 사이 거리 조절하는 IF문
            start = mid + 1
            answer = mid
        else:
            end = mid - 1


binary_search()
print(answer)
