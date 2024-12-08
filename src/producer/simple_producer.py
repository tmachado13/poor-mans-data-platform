from datetime import datetime
import random
from typing import Optional
import requests
from requests.exceptions import RequestException

from .event import Event

class SimpleProducer:
    def __init__(self, event_type: str = "test_event", endpoint_url: Optional[str] = None):
        self.event_type = event_type
        self.endpoint_url = endpoint_url

    def generate_event(self) -> Event:
        """Generate a simple test event with random data."""
        return Event(
            timestamp=datetime.now(),
            event_type=self.event_type,
            payload={
                "value": random.randint(1, 100),
                "message": f"Test event generated at {datetime.now().isoformat()}"
            }
        )
    
    def publish_event(self, event: Optional[Event] = None) -> bool:
        """
        Publish an event to the configured endpoint.
        
        Args:
            event: The event to publish. If None, generates a new event.
            
        Returns:
            bool: True if published successfully, False otherwise.
            
        Raises:
            ValueError: If no endpoint_url is configured.
        """
        if not self.endpoint_url:
            raise ValueError("No endpoint URL configured. Set endpoint_url in constructor.")
        
        if event is None:
            event = self.generate_event()
            
        try:
            response = requests.post(
                self.endpoint_url,
                json=event.to_dict(),
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return True
        except RequestException as e:
            print(f"Failed to publish event: {str(e)}")
            return False
