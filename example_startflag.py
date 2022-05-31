from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *
from pyiwannamaker.level_edit.objects import *


# When there is multiple start flags, the most top-left one will be kid's spawn.

def main():
    level = Level('flags')
    size = level.get_size()
    flags = []
    for x in range(16, size[0], 32):
        for y in range(16, size[1], 32):
            flags.append(StartFlag(x, y))
    level.add_objects(flags)
    level.dump_to_file()

if __name__ == "__main__":
    main()