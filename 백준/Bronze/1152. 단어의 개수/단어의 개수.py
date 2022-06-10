a = str(input())

if a == ' ':
    print(0)
else:
    a = a.strip()
    b = a.count(' ') + 1

    print(b)
