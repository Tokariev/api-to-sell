from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class PriceRatingDto:
    rating: Optional[str] = None
    rating_reason: Optional[str] = None
    threshold: Optional[float] = None

    def to_dict(self):
        return asdict(self)
