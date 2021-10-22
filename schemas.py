from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel


class RenterBase(BaseModel):
    name: str
    phone: str
    activity: str
    meters_required: int
    comments: Optional[str] = None


class RenterCreate(RenterBase):
    pass


class Renters(RenterBase):
    id: int
    name: str
    phone:str
    e_mail:Optional[str]
    activity: Optional[str]
    meters_required: int
    comments: Optional[str]
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name:str

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool


    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str


class Token(BaseModel):
    access_token: str
    token_type: str



class TokenData(BaseModel):
    username: Optional[str] = None
    expires: Optional[datetime]
    scopes: List[str] = []