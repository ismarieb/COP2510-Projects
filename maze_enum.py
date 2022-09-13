# Define enumerated type for directions
# North, south, east, or west
# Edit code below as necessary
from enum import Enum, auto

class MazeDirection (Enum):
  NORTH = auto()
  SOUTH = auto()
  EAST =  auto()
  WEST =  auto()


class Maze:
    # Initializes the maze from a list of strings
    # Each string is one row of the maze
    def __init__(self, maze = ["##########",
                               "#       ##",
                               "## ## #  #",
                               "# #    # #",
                               "#   ###  #",
                               "### #G  ##",
                               "##########"]):
        self.maze = maze

    # Accepts a (row, column) coordinate
    # Returns the maze cell at that position
    # ' ':  empty
    # '#':  wall
    # 'G':  goal
    def get_square(self, coord):
      return self.maze[coord[0]][coord[1]]

    # Accepts (row, col) coordinate and direction
    # Directions:  MazeDirection
    # Returns coordinate after moving
    def get_coordinate(self, row, col, direction):
        if direction == MazeDirection.NORTH:
            row -= 1
        elif direction == MazeDirection.EAST:
            col += 1
        elif direction == MazeDirection.WEST:
            col -= 1
        elif direction == MazeDirection.SOUTH:
            row += 1
        else:
            print(f"Invalid move:  {direction}")
        return [row, col]

    # Accepts a coordinate and direction
    # Returns true if the square in that direction is empty or the goal
    # Returns false if the square in that direction is a wall
    def can_move(self, coordinate, direction):
        coordinate = self.get_coordinate(coordinate[0], coordinate[1], direction)
        if self.get_square(coordinate) == '#':
            return False
        else:
            return True

    # Returns all valid moves (MazeDirections)
    # from the given location
    def get_valid_moves(self, coord):
        valid = []
        if self.can_move(coord, MazeDirection.NORTH):
            valid.append(MazeDirection.NORTH)
        if self.can_move(coord, MazeDirection.EAST):
            valid.append(MazeDirection.EAST)
        if self.can_move(coord, MazeDirection.SOUTH):
            valid.append(MazeDirection.SOUTH)
        if self.can_move(coord, MazeDirection.WEST):
            valid.append(MazeDirection.WEST)
        return valid

# Main code:
if __name__ == "__main__":
    maze = Maze()
    location = [1, 1]
    while maze.get_square(location) != 'G':
        # Get a move
        valid = maze.get_valid_moves(location)
        # list of MazeDirections
        valid_strings = [x.name for x in valid]
        # [x.name for x in valid]:  list of strings
        
        move = MazeDirection[input(f'Enter a move ({", ".join(valid_strings)}):  ').upper()]
        while move not in valid:
            move = MazeDirection[input(f'Enter a move ({", ".join(valid_strings)}):  ').upper()]
        
        # Make the move
        location = maze.get_coordinate(location[0], location[1], move)
        # Repeat until at the goal

    print("You win!")
