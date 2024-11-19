from typing import Any

class Rover:
    def __init__(self):
        self.x = 0  # Position x (position x = 0 de base)
        self.y = 0  # Position y (position y = 0 de base)
        self.direction = 'N' # Orientation : N, S, E, W :
        self.icon = '🚙'

    def moveHandler(self, action : str):
        if self.direction == 'N':
            self.y += (treatMove(action))
        elif self.direction == 'S':
            self.y -= (treatMove(action))
        elif self.direction == 'E':
            self.x += (treatMove(action))
        elif self.direction == 'W':
            self.x -= (treatMove(action))

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


def treatMove(commandMove):
    if commandMove == 'f':
        return 1
    elif commandMove == 'b':
        return -1

def isList(obj : str | list) -> Any:
    if isinstance(obj, list):
        return obj
    else:
        return list(obj)