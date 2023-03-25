import sys

input = sys.stdin.readline

N = int(input())

answer = 0
cnt = 1

temp = 1000 - N

if temp // 500 >= 1:
    answer += temp // 500
    temp = temp % 500

if temp // 100 >= 1:
    answer += temp // 100
    temp = temp % 100

if temp // 50 >= 1:
    answer += temp // 50
    temp = temp % 50

if temp // 10 >= 1:
    answer += temp // 10
    temp = temp % 10

if temp // 5 >= 1:
    answer += temp // 5
    temp = temp % 5

if temp // 1 >= 1:
    answer += temp // 1

print(answer)
