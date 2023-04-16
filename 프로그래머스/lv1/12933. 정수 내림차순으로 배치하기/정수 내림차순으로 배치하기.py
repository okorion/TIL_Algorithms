def solution(n):
    answer = ''
    N = list(map(int, str(n)))
    N.sort(reverse=True)
    for n in N:
        answer += str(n)
    return int(answer)