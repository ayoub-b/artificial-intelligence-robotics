colors = [['red', 'green', 'green', 'red' , 'red'],
          ['red', 'red', 'green', 'red', 'red'],
          ['red', 'red', 'green', 'green', 'red'],
          ['red', 'red', 'red', 'red', 'red']]

measurements = ['green', 'green', 'green' ,'green', 'green']


motions = [[0,0],[0,1],[1,0],[1,0],[0,1]]

sensor_right = 0.7

p_move = 0.8

def show(p):
    for i in range(len(p)):
        print p[i]


p = [
      [0.05, 0.05, 0.05, 0.05 , 0.05],
      [0.05, 0.05, 0.05, 0.05 , 0.05],
      [0.05, 0.05, 0.05, 0.05 , 0.05],
      [0.05, 0.05, 0.05, 0.05 , 0.05]
    ]

def sense(p, Z):
    aux = []
    for k in range(len(p)):
        aux.append([0.0, 0.0, 0.0, 0.0, 0.0])
    s = 0.0
    for i in range(len(p)):
        for j in range(len(p[i])):
            hit = (Z == colors[i][j])
            aux[i][j] = p[i][j] * (hit * sensor_right + (1 - hit) * (1 - sensor_right));
            s = s + aux[i][j];
    for m in range(len(aux)):
        for n in range(len(aux[m])):
            aux[m][n] = aux[m][n]/s
    for m in range(len(aux)):
        s = s + sum(aux[m])
    return aux

def move(p, U):
    aux = []
    for k in range(len(p)):
        aux.append([0.0, 0.0, 0.0, 0.0, 0.0])
    for i in range(len(p)):
        for j in range(len(p[i])):
            x = U[0]
            y = U[1]
            aux[i][j] = p_move*p[(i-x)%len(p)][ (j-y)%len(p[i]) ] + (1-p_move)*p[i][j]
    return aux
    

for k in range(len(measurements)):
    p = move(p, motions[k])
    p = sense(p, measurements[k])

show(p)




