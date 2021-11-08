from typing import List, Optional

from pydantic.main import BaseModel


class From(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str
    username: str
    language_code: Optional[str] = None


class Entities(BaseModel):
    offset: Optional[int] = None
    length: Optional[int] = None
    type: Optional[str] = None


class Chat(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    type: str


class Message(BaseModel):
    message_id: int
    date: int
    text: str
    from_: Optional[From] = None
    chat: Optional[Chat] = None
    entities: List[Optional[Entities]] = None

    class Config:
        # alias the "from" field.
        fields = {"from_": "from"}


class RequestTelegramWebhook(BaseModel):
    update_id: int
    message: Message
