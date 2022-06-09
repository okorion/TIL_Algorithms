a = int(input())
b = 0
c = -1   # for문 안에 if 만족할 시 c = 0이 되어 b 출력, 만족하지 못할 시 c = 1이 되어 -1 출력

if a % 5 == 0 and c == -1:
    b += a//5
    print(b)

else:
    for num in range(a//5, -1, -1):  # num 은 5kg 개수
        if (a - 5*num) % 3 == 0:
            b += num + (a - 5*num) // 3  # 5kg 개수 + 3kg 개수
            c = 0
            break
        else:
            c = 1

if c == 0:
    print(b)
elif c == 1:
    print(-1)