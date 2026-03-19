import heapq, random

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

def add(grid):
    n = len(grid)
    x, y = random.randint(0,n-1), random.randint(0,n-1)
    grid[x][y] = 1

n = 20
grid = [[0]*n for _ in range(n)]
s, t = (0,0), (19,19)
cur = s

while cur != t:
    path = a(grid, cur, t)
    if not path:
        print("No path")
        break
    cur = path[1]
    print(cur)
    if random.random() < 0.3:
        add(grid)

print("Reached" if cur == t else "Failed")