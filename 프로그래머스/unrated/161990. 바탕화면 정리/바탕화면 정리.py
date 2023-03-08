def solution(wallpaper):
    min_x, max_x, min_y, max_y = 51, 0, 51, 0
    
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == '#':
                print([i, j])
                min_x = min(min_x, j)
                max_x = max(max_x, j)
                min_y = min(min_y, i)
                max_y = max(max_y, i)
    
    answer = [min_y, min_x, max_y + 1, max_x + 1]
    
    return answer