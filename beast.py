class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Pos(self.x + other.dx, self.y + other.dy)

class Vec:
    def __init__(self, dx, dy):
        self.dx = dx
        self.dy = dy

    def rotate_left(self):
        self.dx, self.dy = self.dy, -self.dx

    def rotate_right(self):
        self.dx, self.dy = -self.dy, self.dx

import sys

N = int(input())
maze= []
try:
    for line in sys.stdin:
        row = []
        for char in line:
            row.append(char)
        maze.append(row)

except EOFError:
    pass

directions = {'^': Vec(0, -1), '>': Vec(1, 0), 'v': Vec(0, 1), '<': Vec(-1, 0)}
beast_dir = None
beast_pos = None

for y in range(len(maze)):
    for x in range(len(maze[y])):
        if maze[y][x] in directions:
            beast_dir = directions[maze[y][x]]
            beast_pos = Pos(x, y)
            break
    if beast_dir:
        break

moves_count = 0
while moves_count < N:
    right_vec = Vec(-beast_dir.dy, beast_dir.dx)
    right_pos = beast_pos + right_vec

    prev_x, prev_y = beast_pos.x, beast_pos.y

    if maze[right_pos.y][right_pos.x] == '.':
        beast_dir.rotate_right()
        moves_count += 1
        if beast_dir.dx == 0 and beast_dir.dy == -1:
            maze[beast_pos.y][beast_pos.x] = '^'
        elif beast_dir.dx == 0 and beast_dir.dy == 1:
            maze[beast_pos.y][beast_pos.x] = 'v'
        elif beast_dir.dx == 1 and beast_dir.dy == 0:
            maze[beast_pos.y][beast_pos.x] = '>'
        else:
            maze[beast_pos.y][beast_pos.x] = '<'

        for row in maze:
            print(''.join(row), end = "")
        print()  
        beast_pos = beast_pos + beast_dir
        moves_count += 1  
    elif maze[beast_pos.y + beast_dir.dy][beast_pos.x + beast_dir.dx] == '.':
        beast_pos = beast_pos + beast_dir
        moves_count += 1
    else:
        beast_dir.rotate_left()
        moves_count += 1

    maze[prev_y][prev_x] = '.'

    if beast_dir.dx == 0 and beast_dir.dy == -1:
        maze[beast_pos.y][beast_pos.x] = '^'
    elif beast_dir.dx == 0 and beast_dir.dy == 1:
        maze[beast_pos.y][beast_pos.x] = 'v'
    elif beast_dir.dx == 1 and beast_dir.dy == 0:
        maze[beast_pos.y][beast_pos.x] = '>'
    else:
        maze[beast_pos.y][beast_pos.x] = '<'

    for row in maze:
        print(''.join(row), end = "")
    print()

    if moves_count == N:
      break
