import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .object import Object # relative import, '.' means current directory
from .constants import *

class Level:
    def __init__(self, level_name: str='default_level_name') -> None:
        self.head = {
            'name': level_name,
            'version': CURRENT_VERSION,
            'tileset': 1,
            'tileset2': 1,
            'bg': 0,
            'spikes': 1,
            'spikes2': 1,
            'width': 800,
            'height': 608,
            'colors': '5A0200000600000005000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000',
            'scroll_mode': 0,
            'music': 0,
            'num_objects': 0 # dynamic
        }
        self.objects = []

    def dump_to_file(self, file_path: str='') -> None:
        root = Element('sfm_map')
        head = SubElement(root, 'head')
        self.dump_head(head)
        objects = SubElement(root, 'objects')
        self.dump_objects(objects)
        tree = ElementTree(root)
        if file_path:
            tree.write(file_path)
        else:
            tree.write(self.head['name']+'.map')
        print('Level \"' + self.head['name'] + '\" dumped successfully.')

    def dump_head(self, head_element: Element) -> None:
        name = SubElement(head_element, 'name')
        name.text = self.head['name']
        version = SubElement(head_element, 'version')
        version.text = str(self.head['version'])
        tileset = SubElement(head_element, 'tileset')
        tileset.text = str(self.head['tileset'])
        tileset2 = SubElement(head_element, 'tileset2')
        tileset2.text = str(self.head['tileset2'])
        bg = SubElement(head_element, 'bg')
        bg.text = str(self.head['bg'])
        spikes = SubElement(head_element, 'spikes')
        spikes.text = str(self.head['spikes'])
        spikes2 = SubElement(head_element, 'spikes2')
        spikes2.text = str(self.head['spikes2'])
        width = SubElement(head_element, 'width')
        width.text = str(self.head['width'])
        height = SubElement(head_element, 'height')
        height.text = str(self.head['height'])
        colors = SubElement(head_element, 'colors')
        colors.text = self.head['colors']
        scroll_mode = SubElement(head_element, 'scroll_mode')
        scroll_mode.text = str(self.head['scroll_mode'])
        music = SubElement(head_element, 'music')
        music.text = str(self.head['music'])
        num_objects = SubElement(head_element, 'num_objects')
        num_objects.text = str(self.head['num_objects'])

    def dump_objects(self, objects_element: Element) -> None:
        for object in self.objects:
            object.dump(objects_element)

    def add_object(self, object: Object) -> None:
        self.objects.append(object)
        self.head['num_objects'] += 1

    def remove_object(self, object: Object) -> bool:
        if object in self.objects:
            self.objects.remove(object)
            self.head['num_objects'] -= 1
            return True
        else:
            return False

    def get_level_name(self) -> str:
        return self.head['name']
    
    def set_level_name(self, level_name: str) -> None:
        self.head['name'] = level_name

    def get_level_version(self) -> int:
        return self.head['version']

    def set_level_version(self, level_version: int) -> None:
        self.head['version'] = level_version

    def get_level_tileset(self) -> int:
        return self.head['tileset']

    def set_level_tileset(self, level_tileset: int) -> None:
        self.head['tileset'] = level_tileset

    def get_level_tileset2(self) -> int:
        return self.head['tileset2']

    def set_level_tileset2(self, level_tileset2: int) -> None:
        self.head['tileset2'] = level_tileset2

    def get_level_bg(self) -> int:
        return self.head['bg']

    def set_level_bg(self, level_bg: int) -> None:
        self.head['bg'] = level_bg

    def get_level_spikes(self) -> int:
        return self.head['spikes']

    def set_level_spikes(self, level_spikes: int) -> None:
        self.head['spikes'] = level_spikes

    def get_level_spikes2(self) -> int:
        return self.head['spikes2']

    def set_level_spikes2(self, level_spikes2: int) -> None:
        self.head['spikes2'] = level_spikes2

    def get_level_width(self) -> int:
        return self.head['width']

    def set_level_width(self, level_width: int) -> None:
        self.head['width'] = level_width

    def get_level_height(self) -> int:
        return self.head['height']

    def set_level_height(self, level_height: int) -> None:
        self.head['height'] = level_height

    def get_level_colors(self) -> str:
        return self.head['colors']

    def set_level_colors(self, level_colors: str) -> None:
        self.head['colors'] = level_colors

    def get_level_scroll_mode(self) -> int:
        return self.head['scroll_mode']

    def set_level_scroll_mode(self, level_scroll_mode: int) -> None:
        self.head['scroll_mode'] = level_scroll_mode

    def get_level_music(self) -> int:
        return self.head['music']

    def set_level_music(self, level_music: int) -> None:
        self.head['music'] = level_music

    def get_level_num_objects(self) -> int:
        return self.head['num_objects']

    def set_level_num_objects(self, level_num_objects: int) -> None:
        self.head['num_objects'] = level_num_objects

    def get_level_objects(self) -> list:
        return self.objects

    def set_level_objects(self, level_objects: list) -> None:
        self.objects = level_objects

    