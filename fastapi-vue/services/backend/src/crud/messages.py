from fastapi import HTTPException
from tortoise.exceptions import DoesNotExist

from src.database.models import Messages
from src.schemas.token import Status
from src.schemas.messages import MessageOutSchema


async def get_messages():
    return await MessageOutSchema.from_queryset(Messages.all())


async def get_message(message_id) -> MessageOutSchema:
    return await MessageOutSchema.from_queryset_single(Messages.get(id=message_id))


async def create_message(message, current_user) -> MessageOutSchema:
    message_dict = message.dict(exclude_unset=True)
    message_dict["author_id"] = current_user.id
    message_obj = await Messages.create(**message_dict)
    return await MessageOutSchema.from_tortoise_orm(message_obj)


async def update_message(message_id, message, current_user) -> MessageOutSchema:
    try:
        db_message = await MessageOutSchema.from_queryset_single(Messages.get(id=message_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Message {message_id} not found")

    if db_message.author.id == current_user.id:
        await Messages.filter(id=message_id).update(**message.dict(exclude_unset=True))
        return await MessageOutSchema.from_queryset_single(Messages.get(id=message_id))

    raise HTTPException(status_code=403, detail=f"Not authorized to update")


async def delete_message(message_id, current_user) -> Status:
    try:
        db_message = await MessageOutSchema.from_queryset_single(Messages.get(id=message_id))
    except DoesNotExist:
        raise HTTPException(status_code=404, detail=f"Message {message_id} not found")

    if db_message.author.id == current_user.id:
        deleted_count = await Messages.filter(id=message_id).delete()
        if not deleted_count:
            raise HTTPException(status_code=404, detail=f"Message {message_id} not found")
        return Status(message=f"Deleted message {message_id}")

    raise HTTPException(status_code=403, detail=f"Not authorized to delete")