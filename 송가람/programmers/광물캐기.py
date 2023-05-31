def solution(picks, minerals):
    answer = 0
    total = sum(picks)
    cal = [[1,1,1], [5,1,1], [25,5,1]]
    
    if total < len(minerals):
        minerals = minerals[:total*5]

    arr = []
    cap = []
    for m in minerals:
        if m == "diamond":
            cap.append(0)
        elif m == "iron":
            cap.append(1)
        else:
            cap.append(2)
            
        if len(cap) == 5:
            arr.append(cap)
            cap = []
    if cap:
        arr.append(cap)
        
    arr = sorted(arr, key=lambda x: (x.count(0), x.count(1)), reverse=True)

    temp = 0
    cnt = 0
    for i in range(3):
        for _ in range(picks[i]):
            if temp > len(arr)-1 :
                return cnt
            for j in arr[temp]:
                cnt += cal[i][j]
            temp += 1
    return cnt
                    