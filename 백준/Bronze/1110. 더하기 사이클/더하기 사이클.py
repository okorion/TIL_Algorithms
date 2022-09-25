import sys

input = sys.stdin.readline

N = int(input())
Tn = N
cnt = 0

while True:
    a = Tn//10
    b = Tn%10
    c = a + b
    new_N = b*10 + c%10
    
    Tn = new_N
    cnt += 1
    
    if new_N == N:
        print(cnt)
        break
