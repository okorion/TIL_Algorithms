N = input()

for _ in range(int(N)):
    UNIV = int(input())
    MAX_UNIV = ""
    MAX_DRINK = 0

    for u in range(UNIV):
        school, drink = map(str, input().split())
        if int(drink) > MAX_DRINK:
            MAX_UNIV = school
            MAX_DRINK = int(drink)

    print(MAX_UNIV)
