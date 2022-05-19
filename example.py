from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import *
from pyiwannamaker.level_edit.constants import *

# this is an example of how to use the pyiwannamaker library

def main():
    level = Level('A brick')
    block = Object(OBJECT_TYPE_BLOCK, 1, 1)
    level.add_object(block)
    print(level)
    # level = Level.load_from_file('test.xml')


if __name__ == '__main__':
    main()