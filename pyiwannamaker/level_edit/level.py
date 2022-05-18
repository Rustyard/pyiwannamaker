import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .object import Object # relative import, '.' means current directory
from .constants import *

class Level:
    """
    Level class, which is a container for all objects in the level.
    Use this class to create a new level, or to load an existing level.
    """
    def __init__(self, level_name: str='default_level_name') -> None:
        """Create a new level with the given name.

        Args:
            level_name (str, optional): Name of the level. Defaults to 'default_level_name'.
        """
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

    @classmethod
    def load_from_file(cls, file_path: str) -> 'Level':
        """Load a level from a map file.

        Args:
            file_path (str): Path to the map file.

        Returns:
            Level: The loaded level.
        """
        print("This method is not viable yet.")

    def dump_to_file(self, file_path: str='') -> None:
        """Dump the level to a map file.

        Args:
            file_path (str, optional): Path to save the map file. Defaults to ''.
            If no path is given, the level name + '.map' will be used.
        """
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
        """Dump the level's head information to the given element.

        Args:
            head_element (Element): The element to dump the head information to.
        """
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
        """Dump the level's objects to the given element.

        Args:
            objects_element (Element): The element to dump the objects to.
        """
        for object in self.objects:
            object.dump(objects_element)

    def add_object(self, object: Object) -> None:
        """Add an object to the level.

        Args:
            object (Object): The object to add.
        """
        self.objects.append(object)
        self.head['num_objects'] += 1

    def remove_object(self, object: Object) -> bool:
        """Remove an object from the level.

        Args:
            object (Object): The object to remove.

        Returns:
            bool: True if the object was removed, False otherwise.
        """
        if object in self.objects:
            self.objects.remove(object)
            self.head['num_objects'] -= 1
            return True
        else:
            return False

    def get_level_name(self) -> str:
        """Get the level's name.

        Returns:
            str: The level's name.
        """
        return self.head['name']
    
    def set_level_name(self, level_name: str) -> None:
        """Set the level's name.

        Args:
            level_name (str): The new level name.
        """
        self.head['name'] = level_name

    def get_level_version(self) -> int:
        """Get the level's version.

        Returns:
            int: The level's version.
        """
        return self.head['version']

    def set_level_version(self, level_version: int) -> None:
        """Set the level's version.

        Args:
            level_version (int): The new level version.
        """
        self.head['version'] = level_version

    def get_level_tileset(self) -> int:
        """Get the level's tileset.

        Returns:
            int: The level's tileset.
        """
        return self.head['tileset']

    def set_level_tileset(self, level_tileset: int) -> None:
        """Set the level's tileset.

        Args:
            level_tileset (int): The new level tileset.
        """
        self.head['tileset'] = level_tileset

    def get_level_tileset2(self) -> int:
        """Get the level's secondary tileset.

        Returns:
            int: The level's secondary tileset.
        """
        return self.head['tileset2']

    def set_level_tileset2(self, level_tileset2: int) -> None:
        """Set the level's secondary tileset.

        Args:
            level_tileset2 (int): The new level secondary tileset.
        """
        self.head['tileset2'] = level_tileset2

    def get_level_bg(self) -> int:
        """Get the level's background style.

        Returns:
            int: The level's background style.
        """
        return self.head['bg']

    def set_level_bg(self, level_bg: int) -> None:
        """Set the level's background style.

        Args:
            level_bg (int): The new level background style.
        """
        self.head['bg'] = level_bg

    def get_level_spikes(self) -> int:
        """Get the level's spike style.

        Returns:
            int: The level's spike style.
        """
        return self.head['spikes']

    def set_level_spikes(self, level_spikes: int) -> None:
        """Set the level's spike style.

        Args:
            level_spikes (int): The new level spike style.
        """
        self.head['spikes'] = level_spikes

    def get_level_spikes2(self) -> int:
        """Get the level's secondary spike style.

        Returns:
            int: The level's secondary spike style.
        """
        return self.head['spikes2']

    def set_level_spikes2(self, level_spikes2: int) -> None:
        """Set the level's secondary spike style.

        Args:
            level_spikes2 (int): The new level secondary spike style.
        """
        self.head['spikes2'] = level_spikes2

    def get_level_width(self) -> int:
        """Get the level's width.

        Returns:
            int: The level's width.
        """
        return self.head['width']

    def set_level_width(self, level_width: int) -> None:
        """Set the level's width.

        Args:
            level_width (int): The new level width.
        """
        self.head['width'] = level_width

    def get_level_height(self) -> int:
        """Get the level's height.

        Returns:
            int: The level's height.
        """
        return self.head['height']

    def set_level_height(self, level_height: int) -> None:
        """Set the level's height.

        Args:
            level_height (int): The new level height.
        """
        self.head['height'] = level_height

    def get_level_colors(self) -> str:
        """Get the level's colors.

        Returns:
            str: The level's colors.
        """
        return self.head['colors']

    def set_level_colors(self, level_colors: str) -> None:
        """Set the level's colors.

        Args:
            level_colors (str): The new level colors.
        """
        self.head['colors'] = level_colors

    def get_level_scroll_mode(self) -> int:
        """Get the level's scroll mode.

        Returns:
            int: The level's scroll mode.
        """
        return self.head['scroll_mode']

    def set_level_scroll_mode(self, level_scroll_mode: int) -> None:
        """Set the level's scroll mode.

        Args:
            level_scroll_mode (int): The new level scroll mode.
        """
        self.head['scroll_mode'] = level_scroll_mode

    def get_level_music(self) -> int:
        """Get the level's music.

        Returns:
            int: The level's music.
        """
        return self.head['music']

    def set_level_music(self, level_music: int) -> None:
        """Set the level's music.

        Args:
            level_music (int): The new level music.
        """
        self.head['music'] = level_music

    def get_level_num_objects(self) -> int:
        """Get the number of objects in the level.

        Returns:
            int: The number of objects in the level.
        """
        return self.head['num_objects']

    def set_level_num_objects(self, level_num_objects: int) -> None:
        """Set the number of objects in the level.

        Args:
            level_num_objects (int): The new number of objects in the level.
        """
        self.head['num_objects'] = level_num_objects

    def get_level_objects(self) -> list:
        """Get the level's objects.

        Returns:
            list: The level's objects.
        """
        return self.objects

    def set_level_objects(self, level_objects: list) -> None:
        """Set the level's objects.

        Args:
            level_objects (list): The new level objects.
        """
        self.objects = level_objects

    