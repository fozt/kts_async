import uuid

from pydantic import BaseModel, EmailStr, Field


class IUserCreate(BaseModel):
    email: EmailStr


class IUserRead(IUserCreate):
    id: uuid.UUID = Field(alias='id_')
