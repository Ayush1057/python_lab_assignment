a = [[10,20,30],
     [40,50,60],
     [70,80,90]]

b = [[11,22,33],
     [44,55,66],
     [77,88,99]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

for x in range(0,3):
    for y in range(0,3):
        result[x][y] = a[x][y] * b[x][y]

for r in result:
    print(r)
    