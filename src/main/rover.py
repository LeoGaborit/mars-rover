from src.main.mapHandler import MapHandler
from src.main.ressources import isList, oddHandler


def treatMove(commandMove):
    if commandMove == 'f':
        return 1
    elif commandMove == 'b':
        return -1

class Rover:
    def __init__(self):
        self.previous_object = "▓"
        self.x = 0  # Position x (position x = 0 de base)
        self.y = 0  # Position y (position y = 0 de base)
        self.direction = 'N' # Orientation : N, S, E, W :
        self.icon = 'R'
        self.mapHandler = MapHandler()
        self.firstPlaceRover()
        self.update_map()

    def moveHandler(self, action: str):
        # Restaurer l'objet précédent avant le déplacement
        self.restore_previous_object()

        # Sauvegarder le nouvel objet sous le rover
        if self.direction == 'N':
            self.previous_object = self.mapHandler.map[self.y + treatMove(action)][self.x]
        elif self.direction == 'S':
            self.previous_object = self.mapHandler.map[self.y - treatMove(action)][self.x]
        elif self.direction == 'E':
            self.previous_object = self.mapHandler.map[self.y][self.x + treatMove(action)]
        elif self.direction == 'W':
            self.previous_object = self.mapHandler.map[self.y][self.x - treatMove(action)]

        # Mettre à jour la position
        if self.direction == 'N':
            self.y -= treatMove(action)
        elif self.direction == 'S':
            self.y += treatMove(action)
        elif self.direction == 'E':
            self.x += treatMove(action)
        elif self.direction == 'W':
            self.x -= treatMove(action)

        self.mapBorderHandler()

        self.update_map()

    def turn(self, commandTurn):
        directions = ['N', 'W', 'S', 'E']
        if commandTurn == 'l':
            self.direction = directions[(directions.index(self.direction) + 1) % 4]
        elif commandTurn == 'r':
            self.direction = directions[(directions.index(self.direction) - 1) % 4]

    def move(self, commandStr : str):
        commandLst = isList(commandStr)
        for action in commandLst:
            if action in ['f', 'b']:
                self.moveHandler(action)
            elif action in ['l', 'r']:
                self.turn(action)

    def afficher_position(self):
        mapSize = self.mapHandler.size
        print(f"Position : ({self.x - oddHandler((mapSize // 2)) + 1}, {self.y - oddHandler((mapSize // 2)) + 1}), Direction : {self.direction}")

    def obstacleDetection(self, map):
        if map[self.x][self.y] != "▓":
            print('Obstacle found')
            self.moveHandler('f')
            print('Obstacle dodged')
            self.afficher_position()

    def mapBorderHandler(self):
        mapSize = self.mapHandler.size
        if self.x < oddHandler((mapSize // 2))-mapSize: # left border
            self.x = oddHandler((mapSize // 2))

        elif self.x > oddHandler((mapSize + 1)): # right border
            self.x = oddHandler((mapSize // 2))-mapSize

        if self.y < oddHandler((mapSize // 2))-mapSize: # bottom border
            self.y = oddHandler((mapSize // 2))

        elif self.y >= oddHandler((mapSize + 1)): # top border
            self.y = oddHandler((mapSize // 2))-mapSize

    def update_map(self):
        self.mapHandler.generate_map()
        self.mapHandler.map[self.y][self.x] = self.icon

    def restore_previous_object(self):
        self.mapHandler.map[self.y][self.x] = self.previous_object

    def firstPlaceRover(self):
        mapSize = self.mapHandler.size
        self.x = oddHandler((mapSize // 2)) - 1
        self.y = oddHandler((mapSize // 2)) - 1





