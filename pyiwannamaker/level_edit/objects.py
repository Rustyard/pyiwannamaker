import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree

from .object import Object
from .param import Param
from .onevent import OnEvent
from .constants import *

class Spike(Object):
    """The spike object.
    """
    def __init__(self, x: int = 0, y: int = 0, angle: int = 90, scale: float = 1, tileset: int = 0) -> None:
        """Initialize a spike object.

        Args:
            x (int, optional): The x position of the spike. Defaults to 0.
            y (int, optional): The y position of the spike. Defaults to 0.
            angle (int, optional): The angle of the spike, it can be 0(facing right), 90(facing up), 180(facing left), 270(facing down). Defaults to 90.
            scale (float, optional): The scale of the spike. Ranged from 0.2 to 15. Defaults to 1.
            tileset (int, optional): The tileset of the spike, can be 0 or 1. Defaults to 0.
        """
        super().__init__(OBJECT_TYPE_SPIKE, x, y, scale=scale)
        self.sprite_angle = angle
        self.params.append(Param('spike_index', tileset))

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
        super().__init__(OBJECT_TYPE_BLOCK, x, y, scale=scale)
        self.params.append(Param('tileset', tileset))
        
