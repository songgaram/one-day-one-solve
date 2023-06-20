def solution(cap, n, deliveries, pickups):
    answer = 0
    d_point = n-1
    p_point = n-1
    point = 0
    def delivering(start, cap):
        for i in range(start, -1, -1):
            if deliveries[i] > 0:
                diff = cap - deliveries[i]
                if diff > 0:
                    cap -= deliveries[i]
                    deliveries[i] = 0
                    continue
                elif diff <= 0:
                    deliveries[i] = abs(diff)
                    return i
        return i
                
    def pickup(start, cap):
        for i in range(start, -1, -1):
            if pickups[i] > 0:
                diff = cap - pickups[i]
                if diff > 0:
                    cap -= pickups[i]
                    pickups[i] = 0
                    continue
                elif diff <= 0:
                    pickups[i] = abs(diff)
                    return i
        return i

    while True:
        if deliveries[d_point] != 0:
            point = d_point
        if pickups[p_point] != 0:
            point = p_point
        if point:
            answer += ((point + 1)*2)
            d_point = delivering(point, cap)
            p_point = pickup(point, cap)
            d_point, p_point = max(d_point, p_point), max(d_point, p_point)
            point = 0
            continue
        if d_point == 0 and p_point == 0 and deliveries[d_point] == 0 and pickups[p_point] == 0:
            break
        p_point -= 1
        d_point -= 1
    return answer

a = solution(4,	5,[1, 0, 3, 1, 2],[0, 3, 0, 4, 0])
print(a)