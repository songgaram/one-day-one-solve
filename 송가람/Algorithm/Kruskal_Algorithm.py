def find_set(x):
    # x의 대표원소를 찾아서 리턴한다.
    while x != parents[x]:
        x = parents[x]
    return x

"""
N: 정점의 개수 (0번 ~ N-1번)
M: 간선의 개수
edges: 그래프의 간선 정보
"""
N, M = map(int, input().split())
edges = []

for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

# 간선을 비용순으로 오름차순 정렬
edges.sort(key=lambda x: x[2])

# parents : 각 정점의 부모 원소 (초기 설정: 모두 자기 자신)
# cnt : 찾은 간선의 개수
parents = [x for x in range(N+1)]
distance, cnt = 0, 0

for a, b, c in edges:
    parent_a, parent_b = find_set(a), find_set(b)
    # 해당 간선이 사이클을 만들지 않는다면
    if parent_a != parent_b:
        # union 연산을 수행한다. (b의 대표 원소가 a의 대표 원소를 가리키게 한다.)
        if parent_a > parent_b:
            parents[parent_a] = parent_b

        parents[parent_b] = parent_a

        distance += c
        cnt += 1

        # N - 1개의 간선을 모두 찾은 경우, 탐색을 종료한다.
        if cnt >= N - 1:
            break

print(distance)

"""
test case
[[1,7,12], [4,7,13], [1,5,17], [3,5,20], [2,4,24], [1,4,28], [3,6,37], [5,6,45], [2,5,62], [1,2,67], [5,7,73]]
N = 7
M = 11
"""


