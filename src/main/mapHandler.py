from random import randint


map : list
coteCarre = 11
obstacle1 = "•"
obstacle2 = "†"
nbreObstacles = 8

#générer un tableau de 10*10

def generate_map():
    global map
    map = []
    for i in range(coteCarre):
        map.append([])
        for j in range(coteCarre):
            map[i].append("▓")

    #place the map center
    map[coteCarre//2][coteCarre//2]=("X")
    map[0][coteCarre//2]=("N")
    map[coteCarre//2][0]=("W")
    map[coteCarre-1][coteCarre//2]=("S")
    map[coteCarre//2][coteCarre-1]=("E")

    #add 4 obstacles randomly on the map
    for i in range (nbreObstacles):
        x = randint(0, coteCarre-1)
        y = randint(0, coteCarre-1)
        obstacle = randint(1, 2)
        if obstacle == 1:
            map[x][y] = obstacle1
        else:
            map[x][y] = obstacle2
        i -= 1

def display_map():
    for i in range(coteCarre):
        for j in range(coteCarre):
            print(map[i][j], end=" ")
        print()

generate_map()
display_map()