import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree

class Param:
    """Parameter for object and events, must have a unique key and a value."""
    def __init__(self, key: str, val: int) -> None:
        """Initialize a parameter with a key and a value.

        Args:
            key (str): The key of the parameter.
            val (int): The value of the parameter.
        """
        self.key = key
        self.val = val
    
    def dump(self, parent: Element) -> None:
        """Dump the parameter to a xml element that belongs to the parent element.

        Args:
            parent (Element): The parent element.
        """
        param = SubElement(parent, 'param')
        param.set('key', self.key)
        param.set('val', str(self.val))

    def set_val(self, val: int) -> None:
        """Set the value of the parameter.
        
        Args:
            val (int): The new value of the parameter.
        """
        self.val = val

    def get_val(self) -> int:
        """Get the value of the parameter."""
        return self.val

    def get_key(self) -> str:
        """Get the key of the parameter."""
        return self.key

    def __str__(self) -> str:
        return 'param {}={}'.format(self.key, self.val)