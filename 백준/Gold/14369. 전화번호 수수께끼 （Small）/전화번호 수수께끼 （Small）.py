import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

A = [
    ('Z', 'ZERO', 0),
    ('X', 'SIX', 6),
    ('G', 'EIGHT', 8),
    ('S', 'SEVEN', 7),
    ('V', 'FIVE', 5),
    ('F', 'FOUR', 4),
    ('I', 'NINE', 9),
    ('W', 'TWO', 2),
    ('R', 'THREE', 3),
    ('O', 'ONE', 1)
]

for t in range(N):
    temp_dict = defaultdict(int)
    arr = [0] * 10

    for c in input():
        temp_dict[c] += 1

    for k, v, i in A:
        if temp_dict[k] > 0:
            arr[i] = temp_dict[k]    #arr 리스트에 숫자(영어로 저장된) 저장
            for c in v:
                temp_dict[c] -= arr[i]    #겹치는 알파벳 없도록 소거하여 A 순서 설정
                # print(temp_dict)
        arr[i] = str(i) * arr[i]
        # print(arr)
    print(f"Case #{t+1}: {''.join(arr)}")
