n,m = map(int,input().split())
book = list(map(int, input().split()))

plus = []
minus = []
count = []

for i in book:
    if i>0:
        plus.append(i)
    else:
        minus.append(abs(i))

plus.sort(reverse=True)
minus.sort(reverse=True)

for i in range(len(plus)//m):
    count.append(plus[i*m])
if len(plus)%m>0:
    count.append(plus[(len(plus)//m)*m])

for i in range(len(minus)//m):
    count.append(minus[i*m])
if len(minus)%m>0:
    count.append(minus[(len(minus)//m)*m])

count.sort()

result = count.pop()
result += 2*sum(count)

print(result)