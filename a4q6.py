import numpy as np
costs = np.array([
    [16, 20, 12],
    [14, 8, 18],
    [26, 24, 16]
])
supply = np.array([200, 160, 90])
demand = np.array([180, 120, 150])
def north_west_corner(supply, demand):
    alloc = np.zeros((3, 3), dtype=int)
    s, d = supply.copy(), demand.copy()
    i = j = 0
    while i < 3 and j < 3:
        q = min(s[i], d[j])
        alloc[i,j] = q
        s[i] -= q
        d[j] -= q
        if s[i] == 0: i += 1
        else: j += 1
    return alloc
alloc = north_west_corner(supply, demand)
iteration = 0
while True:
    u, v = np.full(3, np.nan), np.full(3, np.nan)
    u[0] = 0
    basic = [(i,j) for i in range(3) for j in range(3) if alloc[i,j] > 0]
    while np.isnan(u).any() or np.isnan(v).any():
        for i, j in basic:
            if not np.isnan(u[i]) and np.isnan(v[j]):
                v[j] = costs[i,j] - u[i]
            elif not np.isnan(v[j]) and np.isnan(u[i]):
                u[i] = costs[i,j] - v[j]
    enter_cell, min_opp = None, 0
    for i in range(3):
        for j in range(3):
            if alloc[i,j] == 0:
                opp = costs[i,j] - (u[i] + v[j])
                if opp < min_opp:
                    min_opp, enter_cell = opp, (i,j)
    if min_opp >= 0: break
    if enter_cell == (0,2):
        loop = [(0,2), (0,1), (1,1), (1,2)]
    elif enter_cell == (1,0):
        loop = [(1,0), (0,0), (0,2), (1,2)]
    else: break 
    theta = min(alloc[i,j] for (i,j) in loop[1::2])
    for idx, (i,j) in enumerate(loop):
        alloc[i,j] += theta if idx%2 ==0 else -theta
    iteration +=1
total_cost = np.sum(alloc * costs)
print(f"Optimal Allocation:\n{alloc}\nTotal Cost: {total_cost} BDT")