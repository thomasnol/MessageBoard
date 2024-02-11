from typing import Optional

from pydantic import BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator

from src.database.models import Messages


MessageInSchema = pydantic_model_creator(
    Messages, name="MessageIn", exclude=["author_id"], exclude_readonly=True)
MessageOutSchema = pydantic_model_creator(
    Messages, name="Message", exclude =[
      "modified_at", "author.password", "author.created_at", "author.modified_at"
    ]
)


class UpdateMessage(BaseModel):
    title: Optional[str]
    content: Optional[str]