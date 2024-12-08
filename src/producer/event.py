from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict
import uuid


@dataclass
class Event:
    timestamp: datetime
    event_type: str
    payload: Dict[str, Any]
    id: str = str(uuid.uuid4())

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp.isoformat(),
            "event_type": self.event_type,
            "payload": self.payload
        }
