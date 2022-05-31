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
        if angle not in [0, 90, 180, 270]:
            raise ValueError('angle must be 0, 90, 180, or 270.')
        if tileset not in [0, 1]:
            raise ValueError('tileset must be 0 or 1.')

        super().__init__(OBJECT_TYPE_SPIKE, x, y, scale=scale)
        self.sprite_angle = angle
        self.add_param(Param('spike_index', tileset))

    def dump(self, parent: Element) -> Element:
        obj = super().dump(parent)
        obj.set('sprite_angle', str(self.sprite_angle))
        return obj

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
        if tileset not in [0, 1]:
            raise ValueError('tileset must be 0 or 1.')

        super().__init__(OBJECT_TYPE_BLOCK, x, y, scale=scale)
        self.add_param(Param('tileset', tileset))

class Cherry(Object):
    """The cherry object.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1, color: int = 0, bounce: int = 0) -> None:
        """Initialize the cherry object.
        
        Args:
            x (int, optional): The x position of the cherry. Defaults to 0.
            y (int, optional): The y position of the cherry. Defaults to 0.
            scale (float, optional): The scale of the cherry. Ranged from 0.2 to 15. Defaults to 1.
            color (int, optional): The color of the cherry, it can be from 0 to 11(see constants.py). Defaults to 0.
            bounce (int, optional): The value to determine if the cherry can bounce off walls while moving, it can be 0(off) or 1(on). Defaults to 0.
        """
        if color not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]:
            raise ValueError('color must be 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, or 11.')
        if bounce not in [0, 1]:
            raise ValueError('bounce must be 0 or 1.')

        super().__init__(OBJECT_TYPE_CHERRY, x, y, scale=scale)
        self.add_param(Param('cherry_color', color))
        self.add_param(Param('bounce', bounce))

class SavePoint(Object):
    """The save point object.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1, grav_type: int = 0) -> None:
        """Initialize the save point object.
        
        Args:
            x (int, optional): The x position of the save point. Defaults to 0.
            y (int, optional): The y position of the save point. Defaults to 0.
            scale (float, optional): The scale of the save point. Ranged from 0.2 to 15. Defaults to 1.
            grav_type (int, optional): The gravity type of the save point, it can be 0(up), 1(down). Defaults to 0.
        """
        if grav_type not in [0, 1]:
            raise ValueError('grav_type must be 0 or 1.')

        super().__init__(OBJECT_TYPE_SAVEPOINT, x, y, scale=scale)
        self.add_param(Param('grav_type', grav_type))

class StartFlag(Object):
    """The start flag object. There should only be one start flag per level, but you still can have multiple start flags in one level.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1, grav_type: int = 0) -> None:
        """Initialize the start flag object.
        
        Args:
            x (int, optional): The x position of the start flag. Defaults to 0.
            y (int, optional): The y position of the start flag. Defaults to 0.
            scale (float, optional): The scale of the start flag. Ranged from 0.2 to 15. Defaults to 1.
            grav_type (int, optional): The gravity type of the start flag, it can be 0(up), 1(down). Defaults to 0.
        """
        if grav_type not in [0, 1]:
            raise ValueError('grav_type must be 0 or 1.')

        super().__init__(OBJECT_TYPE_STARTFLAG, x, y, scale=scale)
        self.add_param(Param('grav_type', grav_type))

class FinishWarp(Object):
    """The finish warp object.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1) -> None:
        """Initialize the finish warp object.
        
        Args:
            x (int, optional): The x position of the finish warp. Defaults to 0.
            y (int, optional): The y position of the finish warp. Defaults to 0.
            scale (float, optional): The scale of the finish warp. Ranged from 0.2 to 15. Defaults to 1.
        """
        
        super().__init__(OBJECT_TYPE_FINISHWARP, x, y, scale=scale)

class MiniSpike(Object):
    """The mini-spike object.
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
        if angle not in [0, 90, 180, 270]:
            raise ValueError('angle must be 0, 90, 180, or 270.')
        if tileset not in [0, 1]:
            raise ValueError('tileset must be 0 or 1.')

        super().__init__(OBJECT_TYPE_MINISPIKE, x, y, scale=scale)
        self.sprite_angle = angle
        self.add_param(Param('spike_index', tileset))

    def dump(self, parent: Element) -> Element:
        obj = super().dump(parent)
        obj.set('sprite_angle', str(self.sprite_angle))
        return obj

class Trigger(Object):
    """The trigger object.
    """
    def __init__(self, x: int = 0, y: int = 0, scale: float = 1, trigger_number: int = 0, trigger_once: int = 1, visible: int = 0) -> None:
        """Initialize the trigger object.
        
        Args:
            x (int, optional): The x position of the trigger. Defaults to 0.
            y (int, optional): The y position of the trigger. Defaults to 0.
            scale (float, optional): The scale of the trigger. Ranged from 0.2 to 15. Defaults to 1.
            trigger_number (int, optional): The trigger number of the trigger, it can be from 0 to 999. Defaults to 0.
            trigger_once (int, optional): Tells if the trigger can be triggered only once or not, it can be 0(infinite trigger) or 1(only trigger once). Defaults to 0.
            visible (int, optional): The visibility of the trigger, it can be 0(invisible) or 1(visible). Defaults to 0.
            """
        if trigger_number not in range(1000):
            raise ValueError('trigger_number must be from 0 to 999.')
        if trigger_once not in [0, 1]:
            raise ValueError('trigger_once must be 0 or 1.')
        if visible not in [0, 1]:
            raise ValueError('visible arg must be 0 or 1.')

        super().__init__(OBJECT_TYPE_TRIGGER, x, y, scale=scale)
        self.add_param(Param('trigger_number', trigger_number))
        self.add_param(Param('visible', visible))
        self.add_param(Param('trigger_once', trigger_once))

class AccelerationField(Object):
    """The acceleration field object.
    """
    def __init__(self, x: int = 0, y: int = 0, angle: int = 90, scale: float = 1) -> None:
        """Initialize the acceleration field object.

        Args:
            x (int, optional): The x position of the field. Defaults to 0.
            y (int, optional): The y position of the field. Defaults to 0.
            angle (int, optional): The angle of the field, it can be 0(facing right), 90(facing up), 180(facing left), 270(facing down). Defaults to 90.
            scale (float, optional): The scale of the field. Defaults to 1.
        """
        if angle not in [0, 90, 180, 270]:
            raise ValueError('angle must be 0, 90, 180, or 270.')

        super().__init__(OBJECT_TYPE_ACCELERATION_FIELD, x, y, scale)
        self.params.append(Param('angle', angle))

        
