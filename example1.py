import math
from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *
from pyiwannamaker.level_edit.objects import *

# this is an example of how to use the pyiwannamaker library

def main():
    level = Level('sigmoid')
    size = level.get_size()
    blocks = []
    for i in range(size[0]):
        x = i
        y = sigmoid_for_level(i)
        blocks.append(Block(x, y, scale=0.2))
        
    level.add_objects(blocks)
    level.dump_to_file('sigmoid.map')
    # level = Level.load_from_file('test.xml')

def sigmoid_for_level(x):
    return -608/(1 + math.exp(-(x-400)/80))+608

if __name__ == '__main__':
    main()