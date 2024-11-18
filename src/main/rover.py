class Rover:
    def __init__(self):
        self.x = 0  # Position x (position x = 0 de base)
        self.y = 0  # Position y (position y = 0 de base)
        self.direction = 'N' # Orientation : N, S, E, W :
        self.icon = '🚙'

    def move(self, commandMove):
        if self.direction == 'N':
            self.y += (treatMove(commandMove))
        elif self.direction == 'S':
            self.y -= (treatMove(commandMove))
        elif self.direction == 'E':
            self.x += (treatMove(commandMove))
        elif self.direction == 'W':
            self.x -= (treatMove(commandMove))

    def turn(self, commandTurn):
        directions = ['N', 'W', 'S', 'E']
        if commandTurn == 'l':
            self.direction = directions[(directions.index(self.direction) + 1) % 4]
        elif commandTurn == 'r':
            self.direction = directions[(directions.index(self.direction) - 1) % 4]

    def moveHandler(self, command : str):
        listActions = command.split()
        for action in command:
            if action in ['f', 'b']:
                self.move(action)
            elif action in ['l', 'r']:
                self.turn(action)

    def afficher_position(self):
        print(f"Position : ({self.x}, {self.y}), Direction : {self.direction}")


def treatMove(commandMove):
    if commandMove == 'f':
        return 1
    elif commandMove == 'b':
        return -1