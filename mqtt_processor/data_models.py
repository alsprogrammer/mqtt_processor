from typing import Dict, Union
from pydantic import BaseModel


class MQTTEvent(BaseModel):
    topic: str
    message: Dict[str, Union[str, int, float, bool]]
