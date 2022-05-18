import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .param import Param

class TriggerEvent:
    """The event that will be triggered by an OnEvent."""
    def __init__(self, event_index: int) -> None:
        """Initialize the TriggerEvent with an event index.

        Args:
            event_index (int): The event index.
        """
        self.event_index = event_index
        self.params = []

    def dump(self, parent: Element) -> None:
        """Dump the TriggerEvent to the parent Element.
        
        Args:
            parent (Element): The parent element.
        """
        event = SubElement(parent, 'event')
        event.set('eventIndex', str(self.event_index))
        for param in self.params:
            param.dump(event)

    def add_param(self, param: Param) -> None:
        """Add a Param to the TriggerEvent.
        
        Args:
            param (Param): The Param to add.
        """
        self.params.append(param)

    def remove_param(self, param: Param) -> bool:
        """Remove a Param from the TriggerEvent.
        
        Args:
            param (Param): The Param to remove.

        Returns:
            True if the Param was removed successfully, False otherwise.
        """
        if param in self.params:
            self.params.remove(param)
            return True
        else:
            return False
