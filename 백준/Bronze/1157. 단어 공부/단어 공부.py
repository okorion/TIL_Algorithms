temp_word = str(input().split())
temp_up = temp_word.upper()

temp_word2 = list(temp_up)

result = []

for _ in temp_up:
    if _ not in result:
        result.append(_)

result = result[2:len(result)-1]


bb = []

for _ in result:
    bb.append(temp_up.count(_))

max_b = max(bb)

if bb.count(max_b) > 1:
    print('?')
else:
    cc = result[bb.index(max_b)]
    print(cc)