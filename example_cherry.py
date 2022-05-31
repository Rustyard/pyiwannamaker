from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *
from pyiwannamaker.level_edit.objects import *

def main():
    level = Level('apples')
    size = level.get_size()
    apples = []
    for x in range(16, size[0], 32):
        for y in range(16, size[1], 32):
            apples.append(Cherry(x, y, color=CHERRY_COLOR_RANDOM))
    level.add_objects(apples)
    level.dump_to_file()

if __name__ == "__main__":
    main()