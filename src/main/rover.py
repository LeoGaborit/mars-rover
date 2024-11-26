from src.main.ressources import isList, oddHandler


def treatMove(commandMove):
    if commandMove == 'f':
        return 1
    elif commandMove == 'b':
        return -1

class Rover:
    def __init__(self):
        self.x = 0  # Position x (position x = 0 de base)
        self.y = 0  # Position y (position y = 0 de base)
        self.direction = 'N' # Orientation : N, S, E, W :
        self.icon = '🚙'

    def moveHandler(self, action : str):
        if self.direction == 'N':
            self.y += (treatMove(action))
            self.mapBorderHandler()
        elif self.direction == 'S':
            self.y -= (treatMove(action))
            self.mapBorderHandler()
        elif self.direction == 'E':
            self.x += (treatMove(action))
            self.mapBorderHandler()
        elif self.direction == 'W':
            self.x -= (treatMove(action))
            self.mapBorderHandler()

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
        print(f"Position : ({self.x}, {self.y}), Direction : {self.direction}")

    def obstacleDetection(self, map):
        if map[self.x][self.y] != "▓":
            print('Obstacle détecté')
            self.moveHandler('f')
            print('Obstacle évité')
            self.afficher_position()

    def mapBorderHandler(self, nb):
        if self.x < oddHandler((nb // 2))-nb: # left border
            self.x = oddHandler((nb // 2))

        elif self.x > oddHandler((nb + 1)): # right border
            self.x = oddHandler((nb // 2))-nb

        if self.y < oddHandler((nb // 2))-nb: # bottom border
            self.y = oddHandler((nb // 2))

        elif self.y >= oddHandler((nb + 1)): # top border
            self.y = oddHandler((nb // 2))-nb




