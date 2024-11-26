from random import randint

class MapHandler:
    def __init__(self, square=11, numb_obstacle=8):
        self.square = square
        self.numb_obstacle = numb_obstacle
        self.map = []
        self.obstacle1 = "•"
        self.obstacle2 = "†"
        self.generate_map()

    def generate_map(self):
        self.map = []
        for i in range(self.square):
            self.map.append([])
            for j in range(self.square):
                self.map[i].append("▓")

        # place the map center
        self.map[self.square // 2][self.square // 2] = "X"
        self.map[0][self.square // 2] = "N"
        self.map[self.square // 2][0] = "W"
        self.map[self.square - 1][self.square // 2] = "S"
        self.map[self.square // 2][self.square - 1] = "E"

        # add obstacles randomly on the map
        for _ in range(self.numb_obstacle):
            x = randint(0, self.square - 1)
            y = randint(0, self.square - 1)
            obstacle = randint(1, 2)
            if obstacle == 1:
                self.map[x][y] = self.obstacle1
            else:
                self.map[x][y] = self.obstacle2

    def display_map(self):
        for i in range(self.square):
            for j in range(self.square):
                print(self.map[i][j], end=" ")
            print()

    def getMapSize(self):
        return self.square