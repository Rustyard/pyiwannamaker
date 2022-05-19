import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .param import Param
from .onevent import OnEvent

class Object:
    """Base class for in-game objects."""
    def __init__(self, type: int, x: int=0, y: int=0) -> None:
        """Initialize an object with a type and position.

        Args:
            type (int): The type of the object.
            x (int, optional): The x position of the object. Defaults to 0.
            y (int, optional): The y position of the object. Defaults to 0.
        """
        self.type = type
        self.x = int(x)
        self.y = int(y)
        self.params = [
            Param('scale', '1')
        ]
        self.events = []
    
    def dump(self, parent: Element) -> Element:
        """Dump the object to a xml element that belongs to the parent element(usually the level).

        Args:
            parent (Element): The parent element.
        """
        obj = SubElement(parent, 'object')
        obj.set('type', str(self.type))
        obj.set('x', str(self.x))
        obj.set('y', str(self.y))
        for param in self.params:
            param.dump(obj)
        for event in self.events:
            event.dump(obj)
        return obj

    def add_param(self, param: Param) -> None:
        """Add a parameter to the object.

        Args:
            param (Param): The parameter to add.
        """
        self.params.append(param)

    def change_param(self, key: str, value: float) -> bool:
        """Change the value of a parameter.

        Args:
            key (str): The key of the parameter to change.
            value (float): The new value.

        Returns:
            bool: True if the parameter was changed, False otherwise.
        """
        for param in self.params:
            if param.get_key() == key:
                param.set_val(value)
                return True
        return False

    def remove_param(self, param: Param) -> bool:
        """Remove a parameter from the object.

        Args:
            param (Param): The parameter to remove.

        Returns:
            bool: True if the parameter was removed, False otherwise.
        """
        if param in self.params:
            self.params.remove(param)
            return True
        else:
            return False
    
    def add_event(self, event: OnEvent) -> None:
        """Add an event to the object.

        Args:
            event (OnEvent): The event to add.
        """
        self.events.append(event)

    def remove_event(self, event: OnEvent) -> bool:
        """Remove an event from the object.

        Args:
            event (OnEvent): The event to remove.

        Returns:
            bool: True if the event was removed, False otherwise.
        """
        if event in self.events:
            self.events.remove(event)
            return True
        else:
            return False

    def adjust_event(self, event: OnEvent, key: str, val: int) -> bool:
        """Adjust a parameter of an event.

        Args:
            event (OnEvent): The event to adjust.
            key (str): The key of the parameter to adjust.
            val (int): The new value.

        Returns:
            bool: True if the event was adjusted, False otherwise.
        """
        for e in self.events:
            if e.event_index == event.event_index:
                for p in e.params:
                    if p.key == key:
                        p.value = val
                        return True
        return False

    def __str__(self) -> str:
        return 'Object(type={}, x={}, y={}, param_count={})'.format(self.type, self.x, self.y, len(self.params))
    