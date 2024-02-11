from typing import List

from fastapi import APIRouter, Depends, HTTPException
from tortoise.contrib.fastapi import HTTPNotFoundError
from tortoise.exceptions import DoesNotExist

import src.crud.messages as crud
from src.auth.jwthandler import get_current_user
from src.schemas.messages import MessageOutSchema, MessageInSchema, UpdateMessage
from src.schemas.token import Status
from src.schemas.users import UserOutSchema

router = APIRouter()

@router.get(
    "/messages",
    response_model=List[MessageOutSchema],
    dependencies=[Depends(get_current_user)],
)
async def get_messages():
    return await crud.get_messages()


@router.get(
    "/message/{message_id}",
    response_model=MessageOutSchema,
    dependencies=[Depends(get_current_user)],
)
async def get_message(message_id: int) -> MessageOutSchema:
    try:
        return await crud.get_message(message_id)
    except DoesNotExist:
        raise HTTPException(
            status_code=404,
            detail="Message does not exist",
        )


@router.post(
    "/messages", response_model=MessageOutSchema, dependencies=[Depends(get_current_user)]
)
async def create_message(
    message: MessageInSchema, current_user: UserOutSchema = Depends(get_current_user)
) -> MessageOutSchema:
    return await crud.create_message(message, current_user)


@router.patch(
    "/message/{message_id}",
    dependencies=[Depends(get_current_user)],
    response_model=MessageOutSchema,
    responses={404: {"model": HTTPNotFoundError}},
)
async def update_message(
    message_id: int,
    message: UpdateMessage,
    current_user: UserOutSchema = Depends(get_current_user),
) -> MessageOutSchema:
    return await crud.update_message(message_id, message, current_user)


@router.delete(
    "/message/{message_id}",
    response_model=Status,
    responses={404: {"model": HTTPNotFoundError}},
    dependencies=[Depends(get_current_user)],
)
async def delete_message(
    message_id: int, current_user: UserOutSchema = Depends(get_current_user)
):
    return await crud.delete_message(message_id, current_user)