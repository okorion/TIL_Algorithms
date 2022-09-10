def solution(a, b):
    mon_day = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]
    
    if (sum(mon_day[:a-1]) + b-1) % 7 == 0:
        return "FRI"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 1:
        return "SAT"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 2:
        return "SUN"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 3:
        return "MON"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 4:
        return "TUE"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 5:
        return "WED"
    elif (sum(mon_day[:a-1]) + b-1) % 7 == 6:
        return "THU"
    