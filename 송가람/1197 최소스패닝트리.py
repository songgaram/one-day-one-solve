import sys
input = sys.stdin.readline

def find_set(x):
    while x != parents[x]:
        x = parents[x]
    return x

V, E = map(int, input().split())
edges = []

for _ in range(E):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

edges.sort(key=lambda x: x[2])
parents = [x for x in range(V+1)]
distance = 0

for a, b, c in edges:
    parent_a, parent_b = find_set(a), find_set(b)
    if parent_a != parent_b:
        distance += c
        if parent_a > parent_b:
            parents[parent_a] = parent_b
            continue
        parents[parent_b] = parent_a

print(distance)