 import heapq, random

def g(n, d):
    return [[1 if random.random() < d else 0 for _ in range(n)] for _ in range(n)]

def h(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def a(grid, s, t):
    n = len(grid)
    q = [(0, s)]
    p, cost = {}, {s: 0}

    while q:
        _, u = heapq.heappop(q)
        if u == t:
            r = []
            while u in p:
                r.append(u)
                u = p[u]
            return [s] + r[::-1]

        x, y = u
        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            v = (x+dx, y+dy)
            if 0 <= v[0] < n and 0 <= v[1] < n and grid[v[0]][v[1]] == 0:
                c = cost[u] + 1
                if v not in cost or c < cost[v]:
                    cost[v] = c
                    heapq.heappush(q, (c + h(v, t), v))
                    p[v] = u
    return None

n = 20
grid = g(n, 0.2)
s, t = (0,0), (19,19)
grid[0][0] = grid[19][19] = 0

path = a(grid, s, t)
print(path if path else "No path")