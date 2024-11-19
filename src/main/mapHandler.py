from random import randint


map : list
square = 11
obstacle1 = "•"
obstacle2 = "†"
numbObstacle = 8

#générer un tableau de 10*10

def generate_map():
    global map
    map = []
    for i in range(square):
        map.append([])
        for j in range(square):
            map[i].append("▓")

    # place the map center
    map[square // 2][square // 2]=("X")
    map[0][square // 2]=("N")
    map[square // 2][0]=("W")
    map[square - 1][square // 2]=("S")
    map[square // 2][square - 1]=("E")

    # add 4 obstacles randomly on the map
    for i in range (numbObstacle):
        x = randint(0, square - 1)
        y = randint(0, square - 1)
        obstacle = randint(1, 2)
        if obstacle == 1:
            map[x][y] = obstacle1
        else:
            map[x][y] = obstacle2
        i -= 1

def display_map():
    for i in range(square):
        for j in range(square):
            print(map[i][j], end=" ")
        print()

generate_map()
display_map()