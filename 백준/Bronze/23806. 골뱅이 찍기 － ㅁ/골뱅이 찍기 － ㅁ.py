N = int(input())

matrix = []

for i in range(N):
    matrix.append('@@@@@'*N)

for j in range(N):
    matrix.append('@'*N + '   '*N + '@'*N)
for k in range(N):
    matrix.append('@'*N + '   '*N + '@'*N)
for l in range(N):
    matrix.append('@'*N + '   '*N + '@'*N)

for z in range(N):
    matrix.append('@@@@@' * N)

for _ in matrix:
    print(_)
