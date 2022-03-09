from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional




class UserCreate(BaseModel):
    email : EmailStr
    password: str
    class Config:
        orm_mode = True

class UserOut(BaseModel):
    id: int
    email: EmailStr 
    created_at: datetime
    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True
    


class Post(PostBase):
    pass
    id: int
    user_id: int
    created_at: datetime
    owner: UserOut
    class Config:
        orm_mode = True


    

class User(BaseModel):
    name : str
    email : str
    password : str
    age : int 

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id : Optional[str]