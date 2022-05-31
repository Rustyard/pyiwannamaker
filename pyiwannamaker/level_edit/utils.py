# basic level layout helper functions
from .level import Level
from .objects import *

def fill_border(level: Level) -> None:
    """Fill the border of the level with walls.
    
    Args:
        level (Level): The level to fill.
    """
    size = level.get_size()
    blocks = []
    # start by filling in with border walls
    for x in range(16, size[0], 32):
        blocks.append(Block(x, 16))
        blocks.append(Block(x, size[1] - 16))
    for y in range(48, size[1] - 32, 32):
        blocks.append(Block(16, y))
        blocks.append(Block(size[0] - 16, y))
    level.add_objects(blocks)