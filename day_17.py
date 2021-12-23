def solve(tl, br):
    velos = []
    for i in range(331):
        for j in range(-100, 1000):
            p = simulate((i, j), (tl, br))
            if p:
                velos.append((i, j))
    print(len(velos))

    
def simulate(starting_velocity, goal):
    vel = starting_velocity
    start = (0, 0)
    pos = start
    step = 0
    ((tlx, tly), (brx, bry)) = goal
    max_height = start
    while (pos[0] <= brx) and (pos[1] >= bry):
        pos = (pos[0]+vel[0], pos[1]+vel[1])
        vel = (max(0, vel[0]-1), vel[1]-1)
        step += 1
        if pos[1] > max_height[1]:
            max_height = pos
        if tlx <= pos[0] <= brx and tly >= pos[1] >= bry:
            print(f"HIT: {pos}, VEL: {starting_velocity}")
            return max_height


if __name__ == "__main__":
    solve((288, -50), (330,-96))
