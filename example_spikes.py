from pyiwannamaker.level_edit.level import Level
from pyiwannamaker.level_edit.object import Object
from pyiwannamaker.level_edit.constants import *
from pyiwannamaker.level_edit.objects import *
import random

def main():
    level = Level('spikes')
    size = level.get_size()
    spikes = []
    for x in range(16, size[0], 32):
        for y in range(16, size[1], 32):
            spikes.append(MiniSpike(x, y, random.choice([0, 90, 180, 270])))
    level.add_objects(spikes)
    level.dump_to_file('level_output/spikes.map')

if __name__ == "__main__":
    main()