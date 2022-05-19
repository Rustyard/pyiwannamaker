import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree

from .object import Object
from .param import Param
from .onevent import OnEvent
from .constants import *

class Spike(Object):
    def __init__(self, x: int = 0, y: int = 0, angle: int = 90, scale: float = 1, tileset: int = 0) -> None:
        super().__init__(OBJECT_TYPE_SPIKE, x, y)
        self.sprite_angle = angle
        self.params.append(Param('spike_index', tileset))
        if scale < 0.2:
            scale = 0.2
        if scale > 15:
            scale = 15
        self.change_param('scale', scale)

    def dump(self, parent: Element) -> None:
        obj = super().dump(parent)
        obj.set('sprite_angle', str(self.sprite_angle))

class Block(Object):
    """The block object.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1, tileset: int = 0) -> None:
        """Initialize the block object.

        Args:
            x (int, optional): The x position of the block. Defaults to 0.
            y (int, optional): The y position of the block. Defaults to 0.
            scale (float, optional): The scale of the block. Ranged from 0.2 to 15. Defaults to 1.
            tileset (int, optional): The tileset value of the block, it's either 0 or 1. Defaults to 0.
        """
        super().__init__(OBJECT_TYPE_BLOCK, x, y)
        self.params.append(Param('tileset', tileset))
        if scale < 0.2:
            scale = 0.2
        if scale > 15:
            scale = 15
        self.change_param('scale', scale)
