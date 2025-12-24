from dataclasses import dataclass
from typing import Optional, Dict, Any

@dataclass
class Message:
    role: str  # user | system | agent
    content: str
    metadata: Optional[Dict[str, Any]] = None
