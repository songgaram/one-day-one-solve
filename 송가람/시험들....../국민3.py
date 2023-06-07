import time, random

ar = random.sample(range(-500000, 500000), 500000)

def solution(n, arr):
    dic = dict()
    ans = [0] * n
    start = 0
    end = n - 1
    for i in range(len(arr)-1, -1, -1):
        if abs(arr[i]) in dic:
            continue
        if arr[i] < 0:
            dic[abs(arr[i])] = end
            ans[end] = abs(arr[i])
            end -= 1
        else:
            dic[arr[i]] = start
            ans[start] = arr[i]
            start += 1
    num = 1
    for j in range(n):
        if ans[j] == 0:
            while num in dic:
                num += 1
            dic[num] = 0
            ans[j] = num

    return ans



start = time.time()
a = solution(7, [1,1,1,1,1,5,5,5,5,1,5,1,-5])
print(a)
end = time.time()
print(end - start)
