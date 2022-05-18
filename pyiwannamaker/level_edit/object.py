import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree

class Object:
    def __init__(self, type: int, x: int=0, y: int=0) -> None:
        self.type = type
        self.x = x
        self.y = y
        self.params = [
            Param('scale', '1')
        ]
    
    def dump(self, parent: Element) -> None:
        obj = SubElement(parent, 'object')
        obj.set('type', str(self.type))
        obj.set('x', str(self.x))
        obj.set('y', str(self.y))
        for param in self.params:
            param.dump(obj)

    def __str__(self) -> str:
        return 'Object(type={}, x={}, y={}, param_count={})'.format(self.type, self.x, self.y, len(self.params))
    
class Param:
    def __init__(self, key: str, val: str) -> None:
        self.key = key
        self.val = val
    
    def dump(self, parent: Element) -> None:
        param = SubElement(parent, 'param')
        param.set('key', self.key)
        param.set('val', self.val)

