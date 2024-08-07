###############
# Maze Solver #
###############

import string


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]


def walk(maze: list[string], wall: string, curr: Point, end: Point, seen: list[list[bool]], path: list[Point]) -> bool:
    if curr.x < 0 or curr.x >= len(maze[0]) or curr.y < 0 or curr.y >= len(maze):
        return False

    if maze[curr.y][curr.x] == wall:
        return False

    if curr.x == end.x and curr.y == end.y:
        path.append(end)
        return True

    if seen[curr.y][curr.x]:
        return False

    # 3 recurse part
    # pre
    seen[curr.y][curr.x] = True
    path.append(curr)

    # recurse
    for i in range(len(dirs)):
        x, y = dirs[i]
        if walk(maze, wall, Point(curr.x + x, curr.y + y), end, seen, path):
            return True

    # post
    path.pop()

    return False


def solve(maze: list[string], wall: string, start: Point, end: Point) -> list[Point]:
    seen = []
    path = []

    for i in range(len(maze)):
        seen.append([])
        for j in range(len(maze[0])):
            seen[i].append(False)

    walk(maze, wall, start, end, seen, path)

    return path


maze = [
    "########E##",
    "####  #  ##",
    "#     #  ##",
    "#S###   ###"
]
wall = '#'
start = Point(1, 3)
end = Point(8, 0)

path = solve(maze, wall, start, end)
char_list = [list(maze_row) for maze_row in maze]
for point in path:
    if char_list[point.y][point.x] == 'E' or char_list[point.y][point.x] == 'S':
        continue
    char_list[point.y][point.x] = 'x'
for i, row in enumerate(char_list):
    char_list[i] = ''.join(row)

print("---THE MAZE---")
for row in maze:
    print(row)

print("\n---SOLVING PATH---")
for row in char_list:
    print(row)
