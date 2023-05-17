n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]

money_list = [0] * n

for i in range(n):
    day, money = table[i]
    cur_d = day + i
    if not money_list[i] and cur_d <= n:
        money_list[i] = money
    if cur_d <= n:
        for j in range(cur_d, n):
            next_d = j + table[j][0]
            if next_d <= n:
                money_list[j] = max(money_list[j], money_list[i] + table[j][1])

print(max(money_list))

# 재귀 실패!
# def calculate_m(idx, money):
#     for i in range(idx, n):
#         day, m = table[i]
#         cur_d = day + i
#         cur_m = money + m
#         if cur_d < n - 1:
#             calculate_m(cur_d, cur_m)
#         elif cur_d == n - 1:
#             if table[-1][0] == 1:
#                 cur_m += table[-1][1]
#                 money_list.append(cur_m)
#                 return cur_m
#             else:
#                 break
#         elif cur_d > n - 1:
#             continue

#     money_list.append(cur_m)
#     return  

# calculate_m(0, 0)
# print(money_list)


