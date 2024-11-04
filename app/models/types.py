from datetime import datetime
from enum import Enum, StrEnum
from typing import Annotated

from pydantic import BeforeValidator


class Gender(str, Enum):
    none = "none"
    na = "n/a"
    male = "male"
    hermaphrodite = "hermaphrodite"
    female = "female"


# Datetime
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
datetime_iso = Annotated[datetime, BeforeValidator(lambda v: datetime.strptime(v, ISO_FORMAT))]

# Colors
possible_colors = ['blond', 'unknown', 'n/a', 'green', 'mottled green', 'green-tan', 'light', 'blue-gray', 'silver',
                   'brown', 'pink', 'none', 'dark', 'grey', 'blue', 'blonde', 'white', 'red', 'pale', 'hazel', 'yellow',
                   'orange', 'metal', 'gold', 'brown mottle', 'tan', 'black', 'auburn', 'fair']

Color = StrEnum('Color', possible_colors)

Colors = Annotated[list[Color], BeforeValidator(lambda vs: [v for v in vs.split(', ')])]
