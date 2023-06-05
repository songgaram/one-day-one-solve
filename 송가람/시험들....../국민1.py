def solution(members, point):
    recommend = dict()
    points = dict()
    

    for i in members:
        p, r = i.split()
        if r == "-":
            continue
        recommend[p] = r
        if r in points:
            points[r] += point
        else:
            points[r] = point
        save = point
        while r in recommend:
            temp = recommend[r]
            point = int(point * 0.1)
            points[temp] += point
            r = temp  
        point = save

    return points

