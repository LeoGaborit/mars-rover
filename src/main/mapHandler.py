from random import randint

class MapHandler:
    def __init__(self, size=11, numb_obstacle=8):
        self.size = size
        self.numb_obstacle = numb_obstacle
        self.map = []
        self.obstacle1 = "•"
        self.obstacle2 = "†"
        self.generate_map()

    def generate_map(self):
        self.map = []
        for i in range(self.size):
            self.map.append([])
            for j in range(self.size):
                self.map[i].append("▓")

        # place the map center
        self.map[self.size // 2][self.size // 2] = "X"
        self.map[0][self.size // 2] = "N"
        self.map[self.size // 2][0] = "W"
        self.map[self.size - 1][self.size // 2] = "S"
        self.map[self.size // 2][self.size - 1] = "E"

        # add obstacles randomly on the map
        for _ in range(self.numb_obstacle):
            x = randint(0, self.size - 1)
            y = randint(0, self.size - 1)
            obstacle = randint(1, 2)
            if obstacle == 1:
                self.map[x][y] = self.obstacle1
            else:
                self.map[x][y] = self.obstacle2

    def display_map(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.map[i][j], end=" ")
            print()

    def getMapSize(self):
        return self.size