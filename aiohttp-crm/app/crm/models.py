import uuid

from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id_: uuid.UUID
    email: EmailStr
