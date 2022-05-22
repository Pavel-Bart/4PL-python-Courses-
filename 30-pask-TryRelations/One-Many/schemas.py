from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str


class ItemCreate(ItemBase):
    pass


class ItemSchema(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    passw: str


class UserSchema(UserBase):
    id: int
    items: list[ItemSchema] = []

    class Config:
        orm_mode = True

