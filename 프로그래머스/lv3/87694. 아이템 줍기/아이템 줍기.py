def solution(rectangle, characterX, characterY, itemX, itemY):
    SIZE = 102
    arr = [[0] * SIZE for _ in range(SIZE)]
    
    for r in rectangle:    # 사각형 칠하기
        for a in range(r[1]*2 - 1, r[3]*2):
            for b in range(r[0]*2 - 1, r[2]*2):
                arr[a][b] = 1
                
    for r in rectangle:    # 사격형 테두리 제외하고 칠하기
        for a in range(r[1]*2, r[3]*2 - 1):
            for b in range(r[0]*2, r[2]*2 - 1):
                arr[a][b] = 0
    
    
    x, y = characterX * 2 - 1, characterY * 2 - 1
    
    arr[y][x] = 0    # 캐릭터 시작위치
    arr[itemY * 2 - 1][itemX * 2 - 1] = 2   # 아이템 위치
    
    temp, result = 0, 0
    
    while True:
        temp += 1
        
        if arr[y][x + 1] > 0:    # 우
            x = x + 1
        elif arr[y][x - 1] > 0:    # 좌
            x = x - 1
        elif arr[y - 1][x] > 0:    # 하
            y = y - 1
        elif arr[y + 1][x] > 0:   # 상
            y = y + 1
        else:
            break
            
        if arr[y][x] == 2:  # 현재 위치가 아이템이면
            result = temp
            
        arr[y][x] = 0   # 방문한 곳은 0으로 처리하며 진행
        
    return min(result, temp - result)//2    # 아이템 발견 이후 출발 지점까지 간 거리 => temp