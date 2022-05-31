from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *
from pyiwannamaker.level_edit.objects import *
import random

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)

def find_object_at_position(objects: list, x: int, y: int) -> list[Object]:
    return [obj for obj in objects if obj.x == x and obj.y == y]

def main():
    level = Level('auto-generated_maze')
    level.set_size(LEVEL_SIZE_2X3[0], LEVEL_SIZE_2X3[1])
    blocks = []
    # start by filling in with border walls
    for x in range(16, level.get_size()[0], 32):
        blocks.append(Block(x, 16))
        blocks.append(Block(x, level.get_size()[1] - 16))
    for y in range(48, level.get_size()[1] - 32, 32):
        blocks.append(Block(16, y))
        blocks.append(Block(level.get_size()[0] - 16, y))

    # add block grid
    grid_line = False
    for y in range(48, level.get_size()[1] - 32, 32):
        grid_line = not grid_line
        empty_slot = False
        for x in range(48, level.get_size()[0] - 32, 32):
            empty_slot = not empty_slot
            if grid_line:
                if not empty_slot:
                    blocks.append(Block(x, y))
            else:
                blocks.append(Block(x, y))
    
    # maze generation
    slots = [[(x, y) for y in range(48, level.get_size()[1] - 32, 64)] for x in range(48, level.get_size()[0] - 32, 64)]
    visited = [[False for y in range(48, level.get_size()[1] - 32, 64)] for x in range(48, level.get_size()[0] - 32, 64)]
    total_count = 0
    for l in visited:
        total_count += len(l)
    visit_count = 0

    stack = Stack()
    x = 0
    y = 0
    stack.push((x, y))
    visited[x][y] = True
    visit_count += 1

    while visit_count < total_count:
        if stack.is_empty():
            break
        else:
            directions = []
            for a, b in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if 0 <= a < len(slots) and 0 <= b < len(slots[a]) and not visited[a][b]:
                    directions.append((a, b))
            if len(directions) == 0: # nowhere to go, backtrack
                x, y = stack.pop()
                continue
            next_x, next_y = random.choice(directions)
            stack.push((next_x, next_y))
            visited[next_x][next_y] = True
            visit_count += 1

            cx, cy = slots[x][y]
            cnext_x, cnext_y = slots[next_x][next_y]
            cdelete_x = cx + (cnext_x - cx) // 2
            cdelete_y = cy + (cnext_y - cy) // 2
            obj_to_delete = find_object_at_position(blocks, cdelete_x, cdelete_y) # dig a path
            for obj in obj_to_delete:
                blocks.remove(obj)
            x = next_x
            y = next_y
            


    level.add_objects(blocks)
    level.dump_to_file('level_output/auto-generated_maze.map')
if __name__ == "__main__":
    main()