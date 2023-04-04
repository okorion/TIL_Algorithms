import sys
input = sys.stdin.readline

N, B = map(int, input().split())

temp_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

answer = ""

while N != 0:
    answer += str(temp_list[N % B])
    N = N // B

print(answer[::-1])
