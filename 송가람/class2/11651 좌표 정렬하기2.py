arr = []
N = int(input())
for _ in range(N):
    arr.append(list(map(int, input().split())))

sorted_arr = sorted(arr, key=lambda x : (x[1], x[0]))

for i in range(N):
    print(sorted_arr[i][0], sorted_arr[i][1])