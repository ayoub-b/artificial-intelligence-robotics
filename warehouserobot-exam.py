# -------------------
# Background Information
#
# In this problem, you will build a planner that helps a robot
# find the shortest way in a warehouse filled with boxes
# that he has to pick up and deliver to a drop zone.
#For example:
#
#warehouse = [[ 1, 2, 3],
#             [ 0, 0, 0],
#             [ 0, 0, 0]]
#dropzone = [2,0] 
#todo = [2, 1]
# Robot starts at the dropzone.
# Dropzone can be in any free corner of the warehouse map.
# todo is a list of boxes to be picked up and delivered to dropzone. 
# Robot can move diagonally, but the cost of diagonal move is 1.5 
# Cost of moving one step horizontally or vertically is 1.0
# If the dropzone is at [2, 0], the cost to deliver box number 2
# would be 5.

# To pick up a box, robot has to move in the same cell with the box.
# When a robot picks up a box, that cell becomes passable (marked 0)
# Robot can pick up only one box at a time and once picked up 
# he has to return it to the dropzone by moving on to the cell.
# Once the robot has stepped on the dropzone, his box is taken away
# and he is free to continue with his todo list.
# Tasks must be executed in the order that they are given in the todo.
# You may assume that in all warehouse maps all boxes are
# reachable from beginning (robot is not boxed in).

# -------------------
# User Instructions
#
# Design a planner (any kind you like, so long as it works).
# This planner should be a function named plan() that takes
# as input three parameters: warehouse, dropzone and todo. 
# See parameter info below.
#
# Your function should RETURN the final, accumulated cost to do
# all tasks in the todo list in the given order and this cost
# must which should match with our answer).
# You may include print statements to show the optimum path,
# but that will have no effect on grading.
#
# Your solution must work for a variety of warehouse layouts and
# any length of todo list.
# Add your code at line 76.
# 
# --------------------
# Parameter Info
#
# warehouse - a grid of values. where 0 means that the cell is passable,
# and a number between 1 and 99 shows where the boxes are.
# dropzone - determines robots start location and place to return boxes 
# todo - list of tasks, containing box numbers that have to be picked up
#
# --------------------
# Testing
#
# You may use our test function below, solution_check
# to test your code for a variety of input parameters. 

warehouse = [[ 1, 2, 3],
             [ 0, 0, 0],
             [ 0, 0, 0]]
dropzone = [2,0] 
todo = [2, 1]

# ------------------------------------------
# plan - Returns cost to take all boxes in the todo list to dropzone
#
# ----------------------------------------
# modify code below
# ----------------------------------------

def lookupfortarget(warehouse, dropzone, target):
    cost = 0
    closed = [[0 for row in range(len(warehouse[0]))] for col in range(len(warehouse))]
    closed[dropzone[0]][dropzone[1]] = 1
    moves = [[0,1], [1,0], [1,1], [1,-1]]
    costs = [1.0, 1.0, 1.5, 1.5]
    
    x = dropzone[0]
    y = dropzone[1]
    g = 0
    open = [[g, x, y]]
    moves = [[0,1], [1,0], [1,1], [1,-1]]
    costs = [1.0, 1.0, 1.5, 1.5]
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    expand = [[-1 for row in range(len(warehouse[0]))] for col in range(len(warehouse))]
    step = 0
    lookup = target
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = g
            step = step + 1
            
            if (warehouse[x][y]==lookup):
                #print 'found target', x, y, g
                found = True
            else:
                for k in range(2):
                    for i in range(len(moves)):
                        x2 = x + moves[i][0]*k + moves[i][0]*(k-1)
                        y2 = y + moves[i][1]*k + moves[i][1]*(k-1)
                        if x2 >= 0 and x2 < len(warehouse) and y2 >=0 and y2 < len(warehouse[0]):
                            if closed[x2][y2] == 0 and (warehouse[x2][y2] == 0 or warehouse[x2][y2] == lookup):
                                g2 = g + costs[i]
                                open.append([g2, x2, y2])
                                closed[x2][y2] = 1
    #for i in range(len(expand)):
    #    print expand[i]
    return x, y, g

def costtodropzone(warehouse, dropzone, position):
    cost = 0
    closed = [[0 for row in range(len(warehouse[0]))] for col in range(len(warehouse))]
    closed[position[0]][position[1]] = 1
    moves = [[0,1], [1,0], [1,1], [1,-1]]
    costs = [1.0, 1.0, 1.5, 1.5]
    
    x = position[0]
    y = position[1]
    warehouse[x][y] = 0
    
    g = 0
    open = [[g, x, y]]
    moves = [[0,1], [1,0], [1,1], [1,-1]]
    costs = [1.0, 1.0, 1.5, 1.5]
    found = False  # flag that is set when search is complete
    resign = False # flag set if we can't find expand
    expand = [[-1 for row in range(len(warehouse[0]))] for col in range(len(warehouse))]
    step = 0
    while not found and not resign:
        if len(open) == 0:
            resign = True
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            x = next[1]
            y = next[2]
            g = next[0]
            expand[x][y] = g
            step = step + 1
            
            if (x== dropzone[0] and y==dropzone[1]):
                #print 'found ', x, y, g
                found = True
            else:
                for k in range(2):
                    for i in range(len(moves)):
                        x2 = x + moves[i][0]*k + moves[i][0]*(k-1)
                        y2 = y + moves[i][1]*k + moves[i][1]*(k-1)
                        if x2 >= 0 and x2 < len(warehouse) and y2 >=0 and y2 < len(warehouse[0]):
                            if closed[x2][y2] == 0 and (warehouse[x2][y2] == 0 or warehouse[x2][y2] == 'x'):
                                g2 = g + costs[i]
                                open.append([g2, x2, y2])
                                closed[x2][y2] = 1
    #for i in range(len(expand)):
    #    print expand[i]
    return x, y, g


def plan(warehouse, dropzone, todo):
    cost = 0
    warehouse[dropzone[0]][dropzone[1]] =0
    for t in todo:
        #print 'lookup for', t, 'in', warehouse
        (x, y, g) = lookupfortarget(warehouse, dropzone, t)
        cost = cost+g
        warehouse[x][y]=0
        #print 'new warehouse', g, cost, warehouse
        (x, y, g) = costtodropzone(warehouse, dropzone, [x,y])
        cost = cost+g
        #print 'cost of drop is', g, cost
        #print '\n'
    print 'my cost is :', cost
    return cost
    
################# TESTING ##################
       
# ------------------------------------------
# solution check - Checks your plan function using
# data from list called test[]. Uncomment the call
# to solution_check to test your code.
#
def solution_check(test, epsilon = 0.00001):
    answer_list = []
    
    import time
    start = time.clock()
    correct_answers = 0
    for i in range(len(test[0])):
        user_cost = plan(test[0][i], test[1][i], test[2][i])
        true_cost = test[3][i]
        if abs(user_cost - true_cost) < epsilon:
            print "\nTest case", i+1, "passed!"
            answer_list.append(1)
            correct_answers += 1
            #print "#############################################"
        else:
            print "\nTest case ", i+1, "unsuccessful. Your answer ", user_cost, "was not within ", epsilon, "of ", true_cost 
            answer_list.append(0)
    runtime =  time.clock() - start
    if runtime > 1:
        print "Your code is too slow, try to optimize it! Running time was: ", runtime
        return False
    if correct_answers == len(answer_list):
        print "\nYou passed all test cases!"
        return True
    else:
        print "\nYou passed", correct_answers, "of", len(answer_list), "test cases. Try to get them all!"
        return False
#Testing environment
# Test Case 1 
warehouse1 = [[ 1, 2, 3],
             [ 0, 0, 0],
             [ 0, 0, 0]]
dropzone1 = [2,0] 
todo1 = [2, 1]
true_cost1 = 9
# Test Case 2
warehouse2 = [[   1, 2, 3, 4],
             [   0, 0, 0, 0],
             [   5, 6, 7, 0],
             [ 'x', 0, 0, 8]] 
dropzone2 = [3,0] 
todo2 = [2, 5, 1]
true_cost2 = 21

# Test Case 3
warehouse3 = [[  1, 2, 3, 4, 5, 6, 7],
             [   0, 0, 0, 0, 0, 0, 0],
             [   8, 9,10,11, 0, 0, 0],
             [ 'x', 0, 0, 0,  0, 0, 12]] 
dropzone3 = [3,0] 
todo3 = [5, 10]
true_cost3 = 18

# Test Case 4
warehouse4 = [[  1,17, 5,18, 9,19, 13],
             [   2, 0, 6, 0,10, 0, 14],
             [   3, 0, 7, 0,11, 0, 15],
             [   4, 0, 8, 0,12, 0, 16],
             [   0, 0, 0, 0, 0, 0, 'x']] 
dropzone4 = [4,6] 
todo4 = [13, 11, 6, 17]
true_cost4 = 41

#plan(warehouse1,dropzone1,todo1)
#plan(warehouse2,dropzone2,todo2)
testing_suite = [[warehouse1, warehouse2, warehouse3, warehouse4],
                [dropzone1, dropzone2, dropzone3, dropzone4],
              [todo1, todo2, todo3, todo4],
             [true_cost1, true_cost2, true_cost3, true_cost4]]


solution_check(testing_suite) #UNCOMMENT THIS LINE TO TEST YOUR CODE
