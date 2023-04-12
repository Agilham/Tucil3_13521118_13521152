from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedItem:
    cost: float
    node: Any=field(compare=False)
    path: Any=field(compare=False)
