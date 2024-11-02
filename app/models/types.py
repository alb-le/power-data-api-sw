from datetime import datetime
from typing import Annotated

from pydantic import BeforeValidator


# Datetime
ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'
datetime_iso = Annotated[datetime, BeforeValidator(lambda v: datetime.strptime(v, ISO_FORMAT))]
