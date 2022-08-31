def solution(arr1, arr2):
    col = len(arr1[0])
    row = len(arr1)
    new_result = []         #new_result = [[0] * col] * row는 안됨. for문에 의해 내부값이 바뀌면 모든 col에 영향.
    
    for i in range(row):
        new_result.append([0] * col)

    for r in range(row):
        for c in range(col):
            new_result[r][c] = arr1[r][c] + arr2[r][c]
    
    return new_result
