from pip import main
from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *

def main():
    level = Level('A brick')
    block = Object(OBJECT_TYPE_BLOCK, 1, 1)
    level.add_object(block)
    level.dump_to_file()


if __name__ == '__main__':
    main()