import xml.etree.ElementTree as etree
from xml.etree.ElementTree import Element, SubElement, ElementTree
from .param import Param
from .triggerevent import TriggerEvent

class OnEvent:
    """The event that will trigger a TriggerEvent."""
    def __init__(self, event_index: int) -> None:
        """Initialize the OnEvent with an event index.

        Args:
            event_index (int): The event index.
        """
        self.event_index = event_index
        self.params = []
        self.trigger_events = []
    
    def dump(self, parent: Element) -> None:
        """Dump the OnEvent to the parent Element.
        
        Args:
            parent (Element): The parent element.
        """
        event = SubElement(parent, 'event')
        event.set('eventIndex', str(self.event_index))
        for param in self.params:
            param.dump(event)
        for trigger_event in self.trigger_events:
            trigger_event.dump(event)

    def add_param(self, param: Param) -> None:
        """Add a parameter to the OnEvent.
        
        Args:
            param (Param): The parameter to add.
        """
        self.params.append(param)

    def remove_param(self, param: Param) -> bool:
        """Remove a parameter from the OnEvent.
        
        Args:
            param (Param): The parameter to remove.

        Returns:
            True if the parameter was removed successfully, False otherwise.
        """
        if param in self.params:
            self.params.remove(param)
            return True
        else:
            return False
    
    def add_trigger_event(self, trigger_event: TriggerEvent) -> None:
        """Add a TriggerEvent to the OnEvent.
        
        Args:
            trigger_event (TriggerEvent): The TriggerEvent to add.
        """
        self.trigger_events.append(trigger_event)

    def remove_trigger_event(self, trigger_event: TriggerEvent) -> bool:
        """Remove a TriggerEvent from the OnEvent.
        
        Args:
            trigger_event (TriggerEvent): The TriggerEvent to remove.

        Returns:
            True if the TriggerEvent was removed successfully, False otherwise.
        """
        if trigger_event in self.trigger_events:
            self.trigger_events.remove(trigger_event)
            return True
        else:
            return False