grid = [[0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 1, 1, 0]]
       
goal = [0, len(grid[0])-1] # Goal is in top right corner


delta = [[-1, 0 ], # go up
         [ 0, -1], # go left
         [ 1, 0 ], # go down
         [ 0, 1 ]] # go right

delta_name = ['^', '<', 'v', '>'] # Use these when creating your policy grid.

success_prob = 0.5                      
failure_prob = (1.0 - success_prob)/2.0 # Probability(stepping left) = prob(stepping right) = failure_prob
collision_cost = 100                    
cost_step = 1        
                     

def stochastic_value():
    value = [[1000 for row in range(len(grid[0]))] for col in range(len(grid))]
    policy = [[' ' for row in range(len(grid[0]))] for col in range(len(grid))]
    policy[goal[0]][goal[1]]='*'
    change = True
    value[goal[0]][goal[1]] = 0
    while change:
        change = False

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if goal[0] == x and goal[1] == y:
                    if value[x][y] > 0:
                        value[x][y] = 0
                        change = True
                elif grid[x][y] == 0:
                    for a in range(len(delta)):
                        x2 = x + delta[a][0]
                        y2 = y + delta[a][1]
                        if x2 >= 0 and x2 < len(grid) and y2 >= 0 and y2 < len(grid[0]) and grid[x2][y2] == 0:
                            v2 = value[x2][y2]*success_prob + cost_step
                            for i in range(2):
                                step = (a + (-1)**i)%4
                                x3 = x + delta[step][0]
                                y3 = y + delta[step][1]
                                if x3 >= 0 and x3 < len(grid) and y3 >= 0 and y3 < len(grid[0]) and grid[x3][y3] == 0:
                                    v2 = v2 + value[x3][y3]*failure_prob
                                else:
                                    v2 = v2 + collision_cost*failure_prob
                            if v2 < value[x][y]:
                                policy[x][y] = delta_name[a]
                                change = True
                                value[x][y] = v2
    for i in range(len(value)):
        print value[i]
    for i in range(len(policy)):
        print policy[i]
    return value, policy

stochastic_value()